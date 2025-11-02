<script lang="ts">
    // 必要なモジュールと型をインポート
    import { fly } from 'svelte/transition';
    import { tossSingleLine, type HexagramLine } from '../utils/divinationLogic';
    import myIcon from '$lib/assets/my_icon.png';
    
    // ===================================
    // ⭐️ 状態管理
    // ===================================

    // ⭐️ Django APIのURL (8000番ポートで動いている前提)
    const API_URL = 'http://127.0.0.1:8000/api/v1/divination/';
    
    /**
     * 6つの爻のリストをDjango APIに送信し、解釈文を取得する
     * @param lines 6つの爻のデータ（HexagramLine[]）
     */
    async function fetchInterpretation(lines: HexagramLine[]) {
        try {
            const response = await fetch(API_URL, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    // DjangoがCORS設定されていることを前提
                },
                // サーバーに送るデータ構造をlines: []の形にする
                body: JSON.stringify({ lines: lines }),
            });

            if (!response.ok) {
                // HTTPエラー処理
                throw new Error(`APIリクエスト失敗: ${response.statusText}`);
            }

            const data = await response.json();
            console.log("Djangoからの結果:", data); // 結果をコンソールで確認
            
            // ⭐️ この結果 (data) をSvelteのリアクティブな変数に格納する
            return data; 

        } catch (error) {
            console.error("解釈の取得中にエラーが発生しました:", error);
            return null; 
        }
    }
    
    // 爻の結果を格納する配列 (初期値は空)
    let hexagramLines: HexagramLine[] = []; 
    
    // 占いが進行中かどうかのフラグ
    let isDivining: boolean = false;
    
    // ===================================
    // ⭐️ 占い実行ロジック
    // ===================================
    
    let apiResult: any = null; // ⭐️ Djangoからの解釈文を格納するリアクティブな変数
    /**
     * 占いを開始し、6つの爻を時間差で生成する
     */
    async function startDivination() {
        if (isDivining) return;
        
        isDivining = true;
        hexagramLines = []; // 結果をリセット
        
        // 6回に分けて爻を生成
        for (let i = 1; i <= 6; i++) { 
            // 500msの遅延を入れてアニメーション効果を出す
            await new Promise(resolve => setTimeout(resolve, 500)); 
            
            // 1回分のコイン投げ（爻の結果）を取得
            const lineResult = tossSingleLine(); 

            // 爻の位置情報（1〜6）を割り当てて完全なラインオブジェクトを作成
            const newLine: HexagramLine = {
                ...lineResult,
                position: i, // 初爻(1)から上爻(6)まで順番に設定
            };
            
            // 配列に新しい爻を追加（SvelteがリアクティブにUIを更新）
            hexagramLines = [...hexagramLines, newLine];
        }

        // ⭐️ 爻の生成が完了したらAPIを呼び出す
        if (hexagramLines.length === 6) {
            apiResult = await fetchInterpretation(hexagramLines);
        }

        isDivining = false;
    }

    // 爻の表示シンボルを返す関数
    function getLineSymbol(line: HexagramLine): string {
        if (line.is_changing) {
            // 変爻のシンボル (老陽: ◯, 老陰: ×)
            return line.line_type === '陽' ? '◯' : '✕';
        } else {
            // 不変の爻のシンボル (少陽: —, 少陰: – –)
            return line.line_type === '陽' ? '—' : '– –';
        }
    }

</script>
<div class="p-4 max-w-lg mx-auto mb-8 bg-white shadow-xl rounded-lg border border-gray-200">
    <h1 class="text-3xl font-extrabold text-center mb-4 text-indigo-700 flex items-center justify-center space-x-2">
        <img src={myIcon} alt="後藤Sysアイコン" class="h-8 w-8 object-contain" />
        <span>後藤Sysの易占い</span>
    </h1>
    
    <div class="space-y-4 text-gray-700">
        <h2 class="text-xl font-bold border-b pb-1 text-indigo-600">このシミュレーターの使い方</h2>
        <p>
            このアプリは、古代中国の知恵である「易経（えききょう）」に基づき、現在の状況と未来の傾向を占うシミュレーションツールです。
            ボタンを押すたびに、仮想の「筮竹（ぜいちく）」または「硬貨」による操作をシミュレートし、合計6回の結果（**六十四卦**）を導き出します。
        </p>
        <ol class="list-decimal list-inside ml-4 text-sm space-y-1">
            <li>「易を振って結果を出す」ボタンを押す。</li>
            <li>6つの爻（こう）が、下から順番に生成されます。</li>
            <li>結果として、**本卦**、**変爻のアドバイス**、**之卦**（変化後の状況）の解釈が表示されます。</li>
        </ol>

        <h2 class="text-xl font-bold border-b pb-1 text-indigo-600">占いの心得</h2>
        <p class="text-sm italic bg-yellow-50 p-3 rounded-md border border-yellow-200">
            易占いは、運命を固定するものではなく、**最善の行動を選ぶための助言**です。
            軽い気持ちで何度も同じ質問を繰り返すのではなく、心を落ち着かせ、**真剣な質問を一度だけ**行うことで、より深い洞察が得られます。
            結果を活かし、前向きな行動のきっかけとしてください。
        </p>
    </div>
</div>

<div class="p-4 max-w-lg mx-auto bg-gray-50 shadow-xl rounded-lg">
    </div>


<div class="p-4 max-w-lg mx-auto bg-gray-50 shadow-xl rounded-lg">
    <!-- <h1 class="text-2xl font-bold text-center mb-6 text-gray-800">後藤Sysの易占い</h1> -->

    <button 
        on:click={startDivination} 
        disabled={isDivining}
        class="w-full py-3 mb-8 text-white font-semibold rounded-lg transition duration-200 
               {isDivining ? 'bg-gray-400 cursor-not-allowed' : 'bg-green-600 hover:bg-green-700'}"
    >
        {isDivining ? '占いの実行中...' : '易を振って結果を出す (6回)'}
    </button>

    <div class="space-y-2 flex flex-col-reverse">
        {#each hexagramLines as line (line.position)}
            <div 
                transition:fly={{ x: -20, duration: 500 }}
                class="flex items-center p-2 rounded-md shadow-sm border 
                       {line.is_changing ? 'bg-yellow-100 border-yellow-500 changing-animation' : 'bg-white border-gray-200'}"
            >
                <span class="font-mono text-xl w-8 text-center">
                    {getLineSymbol(line)}
                </span>
                <span class="ml-4 flex-1">
                    {line.position}爻: {line.line_type}爻 (スコア: {line.score})
                </span>
                {#if line.is_changing}
                    <span class="text-red-600 font-bold text-sm">【変爻】</span>
                {/if}
            </div>
        {/each}
    </div>

</div>
{#if apiResult}
    <div class="mt-8 p-6 bg-blue-50 border-l-4 border-blue-500 rounded-lg">
        <h2 class="text-xl font-bold text-blue-800 mb-4">🔮 占い結果の解釈</h2>
        
        <h3 class="text-lg font-semibold mb-2">本卦: {apiResult.original_hexagram.name} ({apiResult.original_hexagram.yomi})</h3>
        <p class="text-gray-700">【卦辞】{apiResult.original_hexagram.gua_ci_meaning}</p>
        <p class="text-gray-700">【運勢】{apiResult.original_hexagram.fortune_summary}</p>

        {#if apiResult.has_changing_lines}
            <h3 class="text-lg font-semibold mt-4 mb-2 text-red-600">✨ 変爻（アドバイス）</h3>
            {#each apiResult.changing_lines as line}
                <div class="ml-4 border-l pl-3 my-2">
                    <p class="font-medium">第{line.position}爻:</p>
                    <p class="text-sm">爻辞解釈: {line.yao_ci_meaning}</p>
                    <p class="text-red-600 font-semibold text-sm">特別アドバイス: {line.changing_line_special_meaning}</p>
                </div>
            {/each}

            {#if apiResult.changing_hexagram}
                <h3 class="text-lg font-semibold mt-6 mb-2">之卦（変化後の状況）: {apiResult.changing_hexagram.name} ({apiResult.changing_hexagram.yomi})</h3>
                <div class="ml-4 p-3 bg-white border rounded-md">
                    <p class="text-sm font-medium text-gray-800">【之卦の卦辞】</p>
                    <p class="text-sm text-gray-600">{apiResult.changing_hexagram.gua_ci_meaning}</p>
                    <p class="text-sm mt-2 font-medium text-gray-800">【之卦の運勢】</p>
                    <p class="text-sm text-gray-600">{apiResult.changing_hexagram.fortune_summary}</p>
                </div>
            {/if}
        {/if}
    </div>
{/if}

<style lang="postcss">
    /* Tailwind CSSのユーティリティクラスを使い、より詳細なアニメーションをCSSで定義 */
    .changing-animation {
        /* 変爻が出た瞬間に背景を明るく点滅させるアニメーション */
        animation: subtle-blink 1s infinite alternate;
    }

    @keyframes subtle-blink {
        from { box-shadow: 0 0 5px rgba(255, 165, 0, 0.5); }
        to { box-shadow: 0 0 10px rgba(255, 165, 0, 0.8); }
    }
</style>