from django.contrib import admin
from .models import Hexagram, LineText, ThemeAdvice, DivinationResult

# ----------------------------------------------------------------------
# 1. 易卦（64卦）マスターモデルの管理画面設定
# ----------------------------------------------------------------------
@admin.register(Hexagram)
class HexagramAdmin(admin.ModelAdmin):
    list_display = ('hexagram_id', 'name', 'yomi', 'upper_trigram', 'lower_trigram', 'rating')
    list_display_links = ('hexagram_id', 'name')
    search_fields = ('name', 'yomi', 'image_desc', 'gua_ci_meaning')
    list_filter = ('rating', 'upper_trigram', 'lower_trigram')
    ordering = ('hexagram_id',)

# ----------------------------------------------------------------------
# 2. 爻（こう）辞マスターモデルの管理画面設定
# ----------------------------------------------------------------------
@admin.register(LineText)
class LineTextAdmin(admin.ModelAdmin):
    list_display = ('hexagram', 'get_line_position_display', 'yao_ci_text')
    list_filter = ('hexagram__name', 'line_position')
    search_fields = ('hexagram__name', 'yao_ci_meaning')
    autocomplete_fields = ['hexagram'] # 外部キーを検索可能なUIに
    ordering = ('hexagram__hexagram_id', 'line_position')

    def get_line_position_display(self, obj):
        return obj.get_line_position_display()
    get_line_position_display.short_description = '爻の位置'

# ----------------------------------------------------------------------
# 3. テーマ別アドバイスモデルの管理画面設定
# ----------------------------------------------------------------------
@admin.register(ThemeAdvice)
class ThemeAdviceAdmin(admin.ModelAdmin):
    list_display = ('hexagram', 'theme', 'keywords')
    list_filter = ('theme', 'hexagram__name')
    search_fields = ('hexagram__name', 'advice_text', 'keywords')
    autocomplete_fields = ['hexagram']
    ordering = ('hexagram__hexagram_id', 'theme')

# ----------------------------------------------------------------------
# 4. 占い結果履歴モデルの管理画面設定
# ----------------------------------------------------------------------
@admin.register(DivinationResult)
class DivinationResultAdmin(admin.ModelAdmin):
    list_display = ('date_created', 'question', 'original_hexagram', 'changing_hexagram')
    list_filter = ('date_created', 'original_hexagram__name')
    search_fields = ('question',)
    autocomplete_fields = ['original_hexagram', 'changing_hexagram']
    ordering = ('-date_created',)
    readonly_fields = ('date_created',)
