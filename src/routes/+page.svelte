<script lang="ts">
  import { goto } from '$app/navigation';
  import { page } from '$app/stores';
  import Button from '$lib/components/Button.svelte';

  $: if ($page.data.session) {
    goto('/dashboard');
  }
</script>

<main class="min-h-screen flex items-center justify-center bg-gray-50">
  <div class="max-w-md w-full px-6 py-8 bg-white rounded-xl shadow-lg">
    <h1 class="text-3xl font-bold text-center mb-8">Welcome to Scriptive</h1>
    <p class="text-center text-gray-600 mb-8">
      Generate YouTube scripts with AI, trained on your favorite creators' style
    </p>
    <div class="space-y-4">
      <a href="/auth/login">
        <Button class="w-full">Sign In</Button>
      </a>
    </div>
  </div>
</main>