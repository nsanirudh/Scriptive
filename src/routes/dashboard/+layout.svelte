<script lang="ts">
  import { page } from '$app/stores';
  import { goto } from '$app/navigation';
  import { Brain, FileText, LogOut } from 'lucide-svelte';
  import { clsx } from 'clsx';
  import { logout } from '$lib/auth';

  const navigation = [
    { href: '/dashboard/train', label: 'Train', icon: Brain },
    { href: '/dashboard/predict', label: 'Predict', icon: FileText }
  ];

  async function handleSignOut() {
    logout();
    goto('/');
  }
</script>

<div class="min-h-screen bg-gray-50">
  <nav class="bg-white shadow">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between h-16">
        <div class="flex">
          <div class="flex-shrink-0 flex items-center">
            <span class="text-xl font-bold text-primary">Scriptive</span>
          </div>
          
          <div class="hidden sm:ml-6 sm:flex sm:space-x-8">
            {#each navigation as item}
              <a
                href={item.href}
                class={clsx(
                  'inline-flex items-center px-1 pt-1 text-sm font-medium',
                  $page.url.pathname === item.href
                    ? 'border-b-2 border-primary text-gray-900'
                    : 'text-gray-500 hover:border-b-2 hover:border-gray-300 hover:text-gray-700'
                )}
              >
                <svelte:component this={item.icon} class="w-4 h-4 mr-2" />
                {item.label}
              </a>
            {/each}
          </div>
        </div>
        
        <div class="flex items-center">
          <button
            on:click={handleSignOut}
            class="inline-flex items-center px-3 py-2 border border-transparent text-sm font-medium rounded-md text-gray-500 hover:text-gray-700"
          >
            <LogOut class="w-4 h-4 mr-2" />
            Sign Out
          </button>
        </div>
      </div>
    </div>
  </nav>

  <main class="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
    <slot />
  </main>
</div>