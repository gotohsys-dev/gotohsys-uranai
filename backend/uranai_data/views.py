# uranai_data/views.py
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q

from .serializers import DivinationInputSerializer, HexagramOutputSerializer, LineTextOutputSerializer
from .models import Hexagram, LineText, ThemeAdvice

# uranai_data/views.py

# ... インポート文 ...

# ----------------------------------------------------------------------
# ⭐️ 八卦のコードマッピング (爻コード -> 漢字)
# ----------------------------------------------------------------------
TRIGRAM_MAP = {
    '111': '乾', '000': '坤', '001': '艮', '100': '震', 
    '010': '坎', '101': '離', '011': '巽', '110': '兌',
}

# ----------------------------------------------------------------------
# ⭐️ 卦番号を計算する関数 (完成版)
# ----------------------------------------------------------------------

def get_hexagram_id_from_lines(lines_data):
    """
    6つの爻のデータから対応するHexagram ID (1-64) を検索する。
    """
    # 1. 爻の並びをバイナリ文字列に変換 (初爻(0) -> 上爻(5) の順)
    # 陽爻=1, 陰爻=0
    binary_lines = [
        '1' if line['line_type'] == '陽' else '0' 
        for line in sorted(lines_data, key=lambda x: x['position'])
    ]

    # 2. 上卦と下卦のバイナリコードを抽出 (下から上へ)
    # 下卦: 1爻, 2爻, 3爻 (index 0, 1, 2)
    lower_binary = "".join(binary_lines[0:3]) 
    # 上卦: 4爻, 5爻, 6爻 (index 3, 4, 5)
    upper_binary = "".join(binary_lines[3:6])

    # 3. 八卦の漢字名に変換
    lower_trigram_name = TRIGRAM_MAP.get(lower_binary)
    upper_trigram_name = TRIGRAM_MAP.get(upper_binary)
    
    if not lower_trigram_name or not upper_trigram_name:
        # 予期せぬエラーを防ぐため
        raise ValueError("Invalid line data provided for trigram mapping.")

    # 4. データベースから対応する Hexagram ID を検索
    try:
        hexagram = Hexagram.objects.only('hexagram_id').get(
            upper_trigram=upper_trigram_name,
            lower_trigram=lower_trigram_name
        )
        return hexagram.hexagram_id
    except Hexagram.DoesNotExist:
        # このエラーは、データ登録に問題がある場合に発生します
        raise Hexagram.DoesNotExist(
            f"卦が見つかりません: 上卦={upper_trigram_name}, 下卦={lower_trigram_name}"
        )

# ----------------------------------------------------------------------
# ⭐️ 之卦のIDを計算する関数
# ----------------------------------------------------------------------

def get_changing_hexagram_id(lines_data):
    """
    変爻がある場合、変爻の極性を反転させて之卦のIDを計算する。
    """
    # 1. 変化後の爻の並びを生成
    changed_binary_lines = []
    for line in sorted(lines_data, key=lambda x: x['position']):
        if line['is_changing']:
            # 変爻の場合、極性を反転させる (陽→陰, 陰→陽)
            changed_type = '陰' if line['line_type'] == '陽' else '陽'
        else:
            changed_type = line['line_type']
            
        changed_binary_lines.append('1' if changed_type == '陽' else '0')
    
    # 2. 上卦と下卦のバイナリコードを抽出 (下から上へ)
    lower_binary = "".join(changed_binary_lines[0:3])
    upper_binary = "".join(changed_binary_lines[3:6])

    # 3. 八卦の漢字名に変換
    lower_trigram_name = TRIGRAM_MAP.get(lower_binary)
    upper_trigram_name = TRIGRAM_MAP.get(upper_binary)
    
    # 4. データベースから対応する Hexagram ID を検索
    try:
        changing_hexagram = Hexagram.objects.only('hexagram_id').get(
            upper_trigram=upper_trigram_name,
            lower_trigram=lower_trigram_name
        )
        return changing_hexagram.hexagram_id
    except Hexagram.DoesNotExist:
        raise Hexagram.DoesNotExist("之卦が見つかりません。データ登録を確認してください。")


# ----------------------------------------------------------------------
# ⭐️ DivinationAPIView の修正
# ----------------------------------------------------------------------
class DivinationAPIView(APIView):
    def post(self, request, *args, **kwargs):
        # ... シリアライザーの検証 ...
        serializer = DivinationInputSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        lines_data = serializer.validated_data['lines']
        
        # 1. 本卦と之卦のIDを決定する
        try:
            # ⭐️ 完成した関数を使って本卦IDを取得
            original_hexagram_id = get_hexagram_id_from_lines(lines_data)
        except (ValueError, Hexagram.DoesNotExist) as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        # 変爻の有無をチェック
        changing_lines = [line for line in lines_data if line['is_changing']]
        has_changing_lines = len(changing_lines) > 0

        # 之卦のIDを計算
        changing_hexagram_id = None
        if has_changing_lines:
             try:
                # ⭐️ 完成した関数を使って之卦IDを取得
                changing_hexagram_id = get_changing_hexagram_id(lines_data)
             except (ValueError, Hexagram.DoesNotExist) as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        # 2. データベースから解釈文を検索 (以降のロジックは変更なし)
        # ... (中略) ...
        # ----------------------------------------------------
        # 本卦の基本情報
        try:
            original_hexagram = Hexagram.objects.get(pk=original_hexagram_id)
        except Hexagram.DoesNotExist:
            return Response({'error': '本卦が見つかりません。'}, status=status.HTTP_404_NOT_FOUND)
        
        # 変爻の解釈（複数の場合がある）
        changing_line_interpretations = []
        if has_changing_lines:
            # 変爻の爻の位置（1〜6）のリストを取得
            changing_positions = [line['position'] for line in changing_lines]
            
            # 本卦に属し、かつ変爻の位置にある爻辞を検索
            changing_line_qs = LineText.objects.filter(
                hexagram=original_hexagram,
                line_position__in=changing_positions
            )
            changing_line_interpretations = LineTextOutputSerializer(changing_line_qs, many=True).data

        # 之卦の基本情報（変爻がある場合のみ）
        changing_hexagram_data = None
        if has_changing_lines and changing_hexagram_id:
            try:
                changing_hexagram = Hexagram.objects.get(pk=changing_hexagram_id)
                changing_hexagram_data = HexagramOutputSerializer(changing_hexagram).data
            except Hexagram.DoesNotExist:
                changing_hexagram_data = {'error': '之卦が見つかりません。'}
        
        # 3. 結果を整形して返す (以降のロジックは変更なし)
        response_data = {
            'original_hexagram': HexagramOutputSerializer(original_hexagram).data,
            'changing_lines': changing_line_interpretations,
            'changing_hexagram': changing_hexagram_data,
            'has_changing_lines': has_changing_lines,
        }

        return Response(response_data, status=status.HTTP_200_OK)