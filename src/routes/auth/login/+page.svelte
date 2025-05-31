<script lang="ts">
  import { goto } from '$app/navigation';
  import { page } from '$app/stores';
  import Button from '$lib/components/Button.svelte';
  import Input from '$lib/components/Input.svelte';
  import { Mail } from 'lucide-svelte';

  let email = '';
  let loading = false;
  let error: string | null = null;

  $: if ($page.data.session) {
    goto('/dashboard');
  }

  async function handleLogin() {
    try {
      loading = true;
      error = null;
      const { error: err } = await $page.data.supabase.auth.signInWithOtp({
        email,
        options: {
          emailRedirectTo: `${window.location.origin}/auth/callback`
        }
      });
      if (err) throw err;
      alert('Check your email for the login link!');
    } catch (err) {
      error = err.message;
      console.error('Login error:', err);
    } finally {
      loading = false;
    }
  }
</script>

<main class="min-h-screen flex items-center justify-center bg-gray-50">
  <div class="max-w-md w-full px-6 py-8 bg-white rounded-xl shadow-lg">
    <div class="flex justify-center mb-8">
      <Mail class="w-12 h-12 text-primary" />
    </div>
    <h1 class="text-3xl font-bold text-center mb-8">Sign In</h1>
    
    <form on:submit|preventDefault={handleLogin} class="space-y-6">
      <Input
        type="email"
        label="Email"
        bind:value={email}
        placeholder="Enter your email"
        error={error}
        required
      />
      
      <Button type="submit" class="w-full" disabled={loading}>
        {loading ? 'Sending link...' : 'Send Magic Link'}
      </Button>
    </form>
  </div>
</main>