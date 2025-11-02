<script>
    import "../app.css"; // Tailwind CSSのインポートなど
    import { page } from '$app/stores';
	import myIcon from '$lib/assets/my_icon_white.png';
</script>

<div class="min-h-screen flex flex-col">
    <header class="bg-gray-800 text-white shadow-md">
        <nav class="max-w-4xl mx-auto flex justify-between items-center p-4">
            <a href="/" class="flex items-center space-x-2 text-xl font-bold hover:text-indigo-400 transition duration-150">
                {#if myIcon}
                    <img src={myIcon} alt="易占いアイコン" class="h-8 w-8 object-contain" /> 
                {/if}
                <span>後藤Sysの易占い</span>
            </a>
            
            <div class="space-x-4 text-sm">
                <a 
                    href="/privacy" 
                    class="hover:text-indigo-400 transition duration-150"
                    class:font-bold={$page.url.pathname === '/privacy'}
                >
                    プライバシーポリシー
                </a>
                <a 
                    href="/about" 
                    class="hover:text-indigo-400 transition duration-150"
                    class:font-bold={$page.url.pathname === '/about'}
                >
                    サイトについて
                </a>
            </div>
        </nav>
    </header>

    <main class="flex-grow py-8 px-4 bg-gray-100">
        <slot />
    </main>

    <footer class="bg-gray-800 text-white text-center text-xs p-3 border-t border-gray-700">
        <div class="max-w-4xl mx-auto">
            &copy; 2025 後藤Sysの易占い. All Rights Reserved.
            <div class="mt-1 space-x-3">
                <a href="/privacy" class="underline hover:text-indigo-400">プライバシーポリシー</a>
                <a href="/about" class="underline hover:text-indigo-400">サイトについて</a>
            </div>
        </div>
    </footer>
</div>