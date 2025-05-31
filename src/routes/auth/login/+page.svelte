<script lang="ts">
  import { goto } from '$app/navigation';
  import Button from '$lib/components/Button.svelte';
  import Input from '$lib/components/Input.svelte';
  import { Mail } from 'lucide-svelte';
  import { login } from '$lib/auth';

  let email = '';
  let password = '';
  let loading = false;
  let error: string | null = null;

  async function handleLogin() {
    try {
      loading = true;
      error = null;
      
      if (login(email, password)) {
        goto('/dashboard');
      } else {
        error = 'Invalid credentials';
      }
    } catch (err) {
      error = 'An error occurred';
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
      
      <Input
        type="password"
        label="Password"
        bind:value={password}
        placeholder="Enter your password"
        required
      />
      
      <Button type="submit" class="w-full" disabled={loading}>
        {loading ? 'Signing in...' : 'Sign In'}
      </Button>
    </form>
  </div>
</main>