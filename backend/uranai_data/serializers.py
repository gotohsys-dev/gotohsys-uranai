# uranai_data/serializers.py
from rest_framework import serializers
from .models import Hexagram, LineText

# ---------------------------------------------------
# ⭐️ I. フロントエンドからの入力データ用シリアライザー
# SvelteKitから送られてくる1つの爻のデータを定義します
# ---------------------------------------------------
class LineInputSerializer(serializers.Serializer):
    """SvelteKitから送られる1つの爻のデータ構造"""
    position = serializers.IntegerField(min_value=1, max_value=6)
    line_type = serializers.CharField(max_length=1)  # '陽' or '陰'
    is_changing = serializers.BooleanField()


class DivinationInputSerializer(serializers.Serializer):
    """SvelteKitから送られる占い結果全体（6つの爻のリスト）"""
    lines = serializers.ListField(
        child=LineInputSerializer(),
        min_length=6,
        max_length=6
    )


# ---------------------------------------------------
# ⭐️ II. データベースからの出力データ用シリアライザー
# ---------------------------------------------------
class LineTextOutputSerializer(serializers.ModelSerializer):
    """特定の爻（変爻）の解釈を出力するためのシリアライザー"""
    
    # 外部キーのIDではなく、直接爻の位置を表示
    position = serializers.SerializerMethodField()

    class Meta:
        model = LineText
        fields = (
            'position', 
            'yao_ci_text', 
            'yao_ci_meaning', 
            'changing_line_special_meaning'
        )
    
    # 爻の位置を LineText モデルから直接取得
    def get_position(self, obj):
        return obj.line_position


class HexagramOutputSerializer(serializers.ModelSerializer):
    """卦全体の解釈を出力するためのシリアライザー"""
    
    # 関連する爻の解釈データを含めるためのネスト
    # lines = LineTextOutputSerializer(many=True, read_only=True) # 本卦の全爻を出力しないためコメントアウト

    class Meta:
        model = Hexagram
        fields = (
            'hexagram_id',
            'name',
            'yomi',
            'image_desc',
            'gua_ci_meaning',
            'fortune_summary',
            'rating',
        )