<script lang="ts">
  import Button from '$lib/components/Button.svelte';
  import Input from '$lib/components/Input.svelte';
  
  let channelHandle = '';
  let numVideos = 10;
  let loading = false;
  let error: string | null = null;
  
  async function handleSubmit() {
    try {
      loading = true;
      error = null;
      
      const formData = new FormData();
      formData.append('channel_handle', channelHandle);
      formData.append('num_videos', numVideos.toString());
      
      const response = await fetch(`${import.meta.env.PUBLIC_API_URL}/train/style`, {
        method: 'POST',
        body: formData
      });
      
      if (!response.ok) throw new Error('Failed to train style profile');
      
      alert('Style profile created successfully!');
    } catch (err) {
      error = err.message;
    } finally {
      loading = false;
    }
  }
</script>

<div class="bg-white shadow rounded-lg p-6">
  <h1 class="text-2xl font-bold mb-6">Train Style Profile</h1>
  
  <form on:submit|preventDefault={handleSubmit} class="space-y-6 max-w-md">
    <Input
      type="text"
      label="YouTube Channel Handle"
      bind:value={channelHandle}
      placeholder="@channelname"
      error={error}
      required
    />
    
    <div>
      <label class="block text-sm font-medium text-gray-700 mb-1">
        Number of Videos
      </label>
      <input
        type="range"
        bind:value={numVideos}
        min="5"
        max="20"
        step="1"
        class="w-full"
      />
      <p class="text-sm text-gray-500 mt-1">Using {numVideos} videos</p>
    </div>
    
    <Button type="submit" disabled={loading}>
      {loading ? 'Training...' : 'Start Training'}
    </Button>
  </form>
</div>