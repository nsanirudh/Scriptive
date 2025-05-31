<script lang="ts">
	import '../app.postcss';
	import { isAuthenticated } from '$lib/auth';
	import { goto } from '$app/navigation';
	import { page } from '$app/stores';
	import { browser } from '$app/environment';

	$: if (browser && $page.url.pathname.startsWith('/dashboard') && !$isAuthenticated) {
		goto('/auth/login');
	}
</script>

<slot />