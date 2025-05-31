<script lang="ts">
  import { createEventDispatcher } from 'svelte';
  import { Upload } from 'lucide-svelte';
  import { clsx } from 'clsx';

  export let multiple = false;
  export let accept = '*';
  export let error: string | undefined = undefined;

  const dispatch = createEventDispatcher<{
    change: { files: FileList | null };
  }>();

  let dragOver = false;
  let inputElement: HTMLInputElement;

  function handleDragOver(e: DragEvent) {
    e.preventDefault();
    dragOver = true;
  }

  function handleDragLeave() {
    dragOver = false;
  }

  function handleDrop(e: DragEvent) {
    e.preventDefault();
    dragOver = false;
    const files = e.dataTransfer?.files;
    if (files) {
      dispatch('change', { files });
    }
  }

  function handleChange(e: Event) {
    const files = (e.target as HTMLInputElement).files;
    dispatch('change', { files });
  }
</script>

<div
  role="region"
  class={clsx(
    'border-2 border-dashed rounded-lg p-8 text-center transition-colors',
    dragOver ? 'border-primary bg-primary/5' : 'border-gray-300',
    'hover:border-primary hover:bg-primary/5',
    error && 'border-red-500 hover:border-red-500'
  )}
  on:dragover={handleDragOver}
  on:dragleave={handleDragLeave}
  on:drop={handleDrop}
>
  <input
    type="file"
    {multiple}
    {accept}
    class="hidden"
    bind:this={inputElement}
    on:change={handleChange}
  />
  
  <Upload class="w-12 h-12 mx-auto mb-4 text-gray-400" />
  
  <p class="text-sm text-gray-600 mb-2">
    Drag and drop your files here, or
    <button
      type="button"
      class="text-primary hover:underline"
      on:click={() => inputElement.click()}
    >
      browse
    </button>
  </p>
  
  {#if error}
    <p class="text-sm text-red-500 mt-2">{error}</p>
  {/if}
</div>