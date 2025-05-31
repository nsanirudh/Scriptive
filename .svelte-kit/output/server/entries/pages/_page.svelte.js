import { c as create_ssr_component, a as subscribe, v as validate_component } from "../../chunks/ssr.js";
import { g as goto } from "../../chunks/client.js";
import { p as page } from "../../chunks/stores.js";
import { B as Button } from "../../chunks/Button.js";
const Page = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  let $page, $$unsubscribe_page;
  $$unsubscribe_page = subscribe(page, (value) => $page = value);
  {
    if ($page.data.session) {
      goto();
    }
  }
  $$unsubscribe_page();
  return `<main class="min-h-screen flex items-center justify-center bg-gray-50"><div class="max-w-md w-full px-6 py-8 bg-white rounded-xl shadow-lg"><h1 class="text-3xl font-bold text-center mb-8" data-svelte-h="svelte-1lzy9b6">Welcome to Scriptive</h1> <p class="text-center text-gray-600 mb-8" data-svelte-h="svelte-1f0x6lq">Generate YouTube scripts with AI, trained on your favorite creators&#39; style</p> <div class="space-y-4"><a href="/auth/login">${validate_component(Button, "Button").$$render($$result, { class: "w-full" }, {}, {
    default: () => {
      return `Sign In`;
    }
  })}</a></div></div></main>`;
});
export {
  Page as default
};
