<script lang="ts">
  import Button from '$lib/components/Button.svelte';
  import Input from '$lib/components/Input.svelte';
import FileUpload from '$lib/components/FileUpload.svelte';
import { PUBLIC_API_URL } from '$env/static/public';
  
  let channelId = '';
  let topic = '';
  let tone = 'educational';
  let audience = 'general';
  let length = 'medium';
  let files: FileList | null = null;
  let loading = false;
  let error: string | null = null;
  let script: string | null = null;
let uploadProgress: number | null = null;
  
  const tones = ['educational', 'dramatic', 'casual', 'professional'];
  const audiences = ['general', 'beginners', 'intermediate', 'advanced'];
  const lengths = ['short', 'medium', 'long'];

function uploadFilesXhr(filesList: FileList): Promise<string> {
  return new Promise((resolve, reject) => {
    const xhr = new XMLHttpRequest();
    xhr.open('POST', `${PUBLIC_API_URL}/predict/upload-context`);
    xhr.upload.onprogress = (e) => {
      if (e.lengthComputable) {
        uploadProgress = Math.round((e.loaded / e.total) * 100);
      }
    };
    xhr.onload = () => {
      if (xhr.status >= 200 && xhr.status < 300) {
        const data = JSON.parse(xhr.responseText);
        resolve(data.collection_name);
      } else {
        reject(new Error('Failed to upload reference documents'));
      }
    };
    xhr.onerror = () => {
      reject(new Error('Network error while uploading documents'));
    };
    const form = new FormData();
    for (const file of Array.from(filesList)) {
      form.append('files', file);
    }
    xhr.send(form);
  });
}
  
  async function handleSubmit() {
    try {
      loading = true;
      error = null;
      script = null;
      
      let collectionName: string | null = null;
      if (files) {
        uploadProgress = 0;
        try {
          collectionName = await uploadFilesXhr(files);
        } finally {
          uploadProgress = null;
        }
      }

      const formData = new FormData();
      formData.append('channel_id', channelId);
      formData.append('topic', topic);
      formData.append('tone', tone);
      formData.append('audience', audience);
      formData.append('length', length);
      if (collectionName) {
        formData.append('collection_name', collectionName);
      }

      const response = await fetch(`${PUBLIC_API_URL}/predict/script`, {
        method: 'POST',
        body: formData
      });
      
      if (!response.ok) throw new Error('Failed to generate script');
      
      const data = await response.json();
      script = data.script;
    } catch (err) {
      error = err instanceof Error ? err.message : String(err);
    } finally {
      loading = false;
    }
  }
</script>

<div class="bg-white shadow rounded-lg p-6">
  <h1 class="text-2xl font-bold mb-6">Generate Script</h1>
  
  <form on:submit|preventDefault={handleSubmit} class="space-y-6">
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
      <Input
        type="text"
        label="Channel ID"
        bind:value={channelId}
        placeholder="Enter the ID of a trained channel (e.g., veritasium)"
        required
      >
        <p class="mt-1 text-sm text-gray-500">
          This is the ID of a channel you've already trained in the Train tab. The generated script will mimic this channel's style.
        </p>
      </Input>
      
      <Input
        type="text"
        label="Topic"
        bind:value={topic}
        placeholder="What's your video about?"
        required
      />
      
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-1">
          Tone
        </label>
        <select
          bind:value={tone}
          class="w-full px-4 py-2 rounded-lg border border-gray-300 focus:border-primary focus:outline-none focus:ring-2 focus:ring-primary/50"
        >
          {#each tones as t}
            <option value={t}>{t}</option>
          {/each}
        </select>
      </div>
      
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-1">
          Target Audience
        </label>
        <select
          bind:value={audience}
          class="w-full px-4 py-2 rounded-lg border border-gray-300 focus:border-primary focus:outline-none focus:ring-2 focus:ring-primary/50"
        >
          {#each audiences as a}
            <option value={a}>{a}</option>
          {/each}
        </select>
      </div>
      
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-1">
          Length
        </label>
        <select
          bind:value={length}
          class="w-full px-4 py-2 rounded-lg border border-gray-300 focus:border-primary focus:outline-none focus:ring-2 focus:ring-primary/50"
        >
          {#each lengths as l}
            <option value={l}>{l}</option>
          {/each}
        </select>
      </div>
    </div>
    
    <div>
      <label class="block text-sm font-medium text-gray-700 mb-1">
        Reference Documents (Optional)
      </label>
      <FileUpload
        multiple
        accept=".pdf,.docx,.txt"
        error={error ?? undefined}
        on:change={({ detail }) => files = detail.files}
      />
      {#if files?.length}
        <ul class="mt-2 text-sm text-gray-700">
          {#each Array.from(files) as file}
            <li>{file.name} ({Math.round(file.size / 1024)} KB)</li>
          {/each}
        </ul>
      {/if}
      {#if uploadProgress !== null}
        <div class="mt-2">
          <progress value={uploadProgress} max="100" class="w-full"></progress>
          <p class="text-sm text-gray-600 mt-1">{uploadProgress}% uploaded</p>
        </div>
      {/if}
    </div>
    
    <Button type="submit" disabled={loading}>
      {loading ? 'Generating...' : 'Generate Script'}
    </Button>
  </form>
  
  {#if script}
    <div class="mt-8">
      <h2 class="text-xl font-semibold mb-4">Generated Script</h2>
      <div class="bg-gray-50 p-4 rounded-lg whitespace-pre-wrap">
        {script}
      </div>
    </div>
  {/if}
</div>