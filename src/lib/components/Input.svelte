<script lang="ts">
  import { clsx } from 'clsx';
  import type { HTMLInputAttributes } from 'svelte/elements';
  import { onMount } from 'svelte';

  interface $$Props extends HTMLInputAttributes {
    label?: string;
    error?: string;
    class?: string;
  }

  export let label: $$Props['label'] = undefined;
  export let error: $$Props['error'] = undefined;
  export let type: $$Props['type'] = 'text';
  export let value: $$Props['value'] = '';
  export let placeholder: $$Props['placeholder'] = '';
  export let disabled: $$Props['disabled'] = false;

  $: className = clsx(
    'w-full px-4 py-2 rounded-lg border bg-white transition-colors',
    error ? 'border-red-500 focus:border-red-500' : 'border-gray-300 focus:border-primary',
    'focus:outline-none focus:ring-2',
    error ? 'focus:ring-red-500/50' : 'focus:ring-primary/50',
    'disabled:opacity-50 disabled:cursor-not-allowed',
    $$props.class
  );

  let inputId = '';
  onMount(() => {
    inputId = 'input-' + Math.random().toString(36).slice(2, 10);
  });
</script>

{#if label}
  <label class="block text-sm font-medium text-gray-700 mb-1" for={inputId}>
    {label}
  </label>
{/if}

<input
  id={inputId}
  {type}
  value={value}
  on:input={(e) => value = e.currentTarget.value}
  {placeholder}
  {disabled}
  class={className}
  aria-invalid={!!error}
  aria-errormessage={error ? `error-${inputId}` : undefined}
  {...$$restProps}
/>

{#if error}
  <p class="mt-1 text-sm text-red-500" id="error-{inputId}">{error}</p>
{/if}