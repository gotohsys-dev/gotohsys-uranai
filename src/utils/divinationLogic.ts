// src/utils/divinationLogic.ts

// ⭐️ 爻のデータ構造を定義するインターフェースをエクスポート
export interface HexagramLine {
    position: number;
    line_type: '陽' | '陰'; // '陽' or '陰'
    score: number; // 6, 7, 8, 9
    is_changing: boolean; // 変爻フラグ
}

/**
 * 3枚のコインを振り、1つの爻の結果（HexagramLine型）を返す関数
 * この関数が 'tossSingleLine' の役割を果たします。
 */
export function tossSingleLine(): Omit<HexagramLine, 'position'> {
    let score = 0;
    // 3回コインを振る
    for (let i = 0; i < 3; i++) {
        score += (Math.random() < 0.5) ? 2 : 3;
    }

    let result: Omit<HexagramLine, 'position'> = { // positionを除く型
        line_type: '陽', // 初期値
        score: score,
        is_changing: false 
    };

    switch (score) {
        case 6: // 老陰 (変化する陰)
            result.line_type = '陰';
            result.is_changing = true;
            break;
        case 7: // 少陽
            result.line_type = '陽';
            break;
        case 8: // 少陰
            result.line_type = '陰';
            break;
        case 9: // 老陽 (変化する陽)
            result.line_type = '陽';
            result.is_changing = true;
            break;
    }
    return result;
}

// 従来の generateHexagram は使わない場合は削除するか、このまま残してもOKです。
// export function generateHexagram() { /* ... */ }