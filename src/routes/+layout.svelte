<script lang="ts">
	import '../app.postcss';
	import { isAuthenticated } from '$lib/auth';
	import { goto } from '$app/navigation';
	import { page } from '$app/stores';

	$: if ($page.url.pathname.startsWith('/dashboard') && !$isAuthenticated) {
		goto('/auth/login');
	}
</script>

<slot />