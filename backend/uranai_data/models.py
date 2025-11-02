# python manage.py makemigrations uranai_data マイグレーションファイルの作成
# python manage.py migrate # データベースの初期化
# python manage.py runserver # 開発サーバーの起動

from django.db import models

# ----------------------------------------------------------------------
# 1. 易卦（64卦）マスターモデル
# ----------------------------------------------------------------------
class Hexagram(models.Model):
    """易占いの64卦の基本情報と解釈を格納するマスターテーブル"""

    # 卦の識別情報
    hexagram_id = models.IntegerField(primary_key=True, verbose_name="卦番号 (1-64)")
    name = models.CharField(max_length=10, unique=True, verbose_name="卦名 (例: 乾為天)")
    yomi = models.CharField(max_length=10, verbose_name="読み方 (例: けんいてん)")

    # 卦の構成要素
    UPPER_TRIGRAM_CHOICES = [
        ('乾', '天'), ('坤', '地'), ('震', '雷'), ('巽', '風'),
        ('坎', '水'), ('離', '火'), ('艮', '山'), ('兌', '沢'),
    ]
    upper_trigram = models.CharField(max_length=2, choices=UPPER_TRIGRAM_CHOICES, verbose_name="上卦")
    lower_trigram = models.CharField(max_length=2, choices=UPPER_TRIGRAM_CHOICES, verbose_name="下卦")

    # 基本解釈
    image_desc = models.TextField(verbose_name="卦の象 (イメージ)")
    gua_ci_meaning = models.TextField(verbose_name="卦辞の基本解釈")
    fortune_summary = models.TextField(verbose_name="運勢（総合的な流れ）")

    # 吉凶の評価
    RATING_CHOICES = [
        ('大吉', '大吉'), ('吉', '吉'), ('中吉', '中吉'),
        ('小吉', '小吉'), ('平', '平'), ('小凶', '小凶'),
        ('凶', '凶'), ('大凶', '大凶'),
    ]
    rating = models.CharField(max_length=4, choices=RATING_CHOICES, default='平', verbose_name="総合吉凶")

    class Meta:
        verbose_name = "易卦 (64卦)"
        verbose_name_plural = "易卦 (64卦)"
        ordering = ['hexagram_id']

    def __str__(self):
        return f"{self.hexagram_id:02d}. {self.name} ({self.yomi})"

# ----------------------------------------------------------------------
# 2. 爻（こう）辞マスターモデル
# ----------------------------------------------------------------------
class LineText(models.Model):
    """各卦の各爻（初爻〜上爻）の詳細な解釈を格納するテーブル"""

    # 外部キー: 所属する卦
    hexagram = models.ForeignKey(
        Hexagram,
        on_delete=models.CASCADE,
        related_name='lines',
        verbose_name="所属卦"
    )

    # 爻の位置
    LINE_POSITION_CHOICES = [
        (1, '初爻'), (2, '二爻'), (3, '三爻'),
        (4, '四爻'), (5, '五爻'), (6, '上爻'),
    ]
    line_position = models.IntegerField(choices=LINE_POSITION_CHOICES, verbose_name="爻の位置")

    # 爻の解釈
    yao_ci_text = models.CharField(max_length=50, blank=True, null=True, verbose_name="爻辞 (古典文言)")
    yao_ci_meaning = models.TextField(verbose_name="爻辞の現代語解釈")
    changing_line_special_meaning = models.TextField(
        blank=True,
        null=True,
        verbose_name="変爻時の特別な意味・アドバイス"
    )

    class Meta:
        verbose_name = "爻辞"
        verbose_name_plural = "爻辞"
        # 複合ユニーク制約: 1つの卦で同じ位置の爻は存在しない
        unique_together = ('hexagram', 'line_position')
        ordering = ['hexagram', 'line_position']

    def __str__(self):
        return f"{self.hexagram.name} - {self.get_line_position_display()} ({self.yao_ci_text or 'なし'})"

# ----------------------------------------------------------------------
# 3. テーマ別アドバイスモデル
# ----------------------------------------------------------------------
class ThemeAdvice(models.Model):
    """特定のテーマ（恋愛、仕事など）に特化したアドバイスを格納するテーブル"""

    # 外部キー: 対象となる卦
    hexagram = models.ForeignKey(
        Hexagram,
        on_delete=models.CASCADE,
        related_name='theme_advices',
        verbose_name="対象卦"
    )

    # テーマ
    THEME_CHOICES = [
        ('恋愛', '恋愛'), ('仕事', '仕事'), ('金運', '金運'),
        ('健康', '健康'), ('対人', '対人関係'), ('願望', '願望・目標')
    ]
    theme = models.CharField(max_length=4, choices=THEME_CHOICES, verbose_name="テーマ")

    # アドバイスの詳細
    advice_text = models.TextField(verbose_name="テーマ別詳細アドバイス")
    keywords = models.CharField(max_length=100, blank=True, null=True, verbose_name="キーワード")

    class Meta:
        verbose_name = "テーマ別アドバイス"
        verbose_name_plural = "テーマ別アドバイス"
        # 複合ユニーク制約: 1つの卦で同じテーマは存在しない
        unique_together = ('hexagram', 'theme')

    def __str__(self):
        return f"{self.hexagram.name} - {self.theme}アドバイス"

# ----------------------------------------------------------------------
# 補助的なテーブル（占いの結果を記録する場合）
# ----------------------------------------------------------------------
class DivinationResult(models.Model):
    """ユーザーの占いの履歴と結果を記録するテーブル"""

    # ユーザー情報（認証システムと連携する場合）
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    # 占いの基本情報
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="占い日時")
    question = models.CharField(max_length=255, verbose_name="質問内容", blank=True, null=True)

    # 本卦（出た卦）
    original_hexagram = models.ForeignKey(
        Hexagram,
        on_delete=models.PROTECT, # 卦マスターは保護
        related_name='results_original',
        verbose_name="本卦"
    )

    # 之卦（変化後の卦）
    # 変爻がない場合もあるため null=True
    changing_hexagram = models.ForeignKey(
        Hexagram,
        on_delete=models.PROTECT,
        related_name='results_changing',
        verbose_name="之卦",
        null=True,
        blank=True
    )

    # 変爻の情報
    # どの爻が変爻したかを格納（例: "2, 5" → 二爻と五爻が変爻）
    changing_lines_list = models.CharField(max_length=10, blank=True, null=True, verbose_name="変爻のリスト")

    class Meta:
        verbose_name = "占い結果履歴"
        verbose_name_plural = "占い結果履歴"
        ordering = ['-date_created']

    def __str__(self):
        return f"結果: {self.original_hexagram.name} ({self.date_created.strftime('%Y-%m-%d')})"