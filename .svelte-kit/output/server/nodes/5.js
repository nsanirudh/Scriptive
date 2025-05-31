

export const index = 5;
let component_cache;
export const component = async () => component_cache ??= (await import('../entries/pages/dashboard/_page.svelte.js')).default;
export const imports = ["_app/immutable/nodes/5.BUB434fD.js","_app/immutable/chunks/bNphU090.js","_app/immutable/chunks/P-961bDU.js","_app/immutable/chunks/ehUx1xvm.js"];
export const stylesheets = [];
export const fonts = [];
