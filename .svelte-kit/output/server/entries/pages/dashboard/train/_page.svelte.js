import { c as create_ssr_component, v as validate_component, f as add_attribute, e as escape } from "../../../../chunks/ssr.js";
import { B as Button } from "../../../../chunks/Button.js";
import { I as Input } from "../../../../chunks/Input.js";
const Page = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  let channelHandle = "";
  let numVideos = 10;
  let loading = false;
  let error = null;
  let $$settled;
  let $$rendered;
  let previous_head = $$result.head;
  do {
    $$settled = true;
    $$result.head = previous_head;
    $$rendered = `<div class="bg-white shadow rounded-lg p-6"><h1 class="text-2xl font-bold mb-6" data-svelte-h="svelte-1767ffq">Train Style Profile</h1> <form class="space-y-6 max-w-md">${validate_component(Input, "Input").$$render(
      $$result,
      {
        type: "text",
        label: "YouTube Channel Handle",
        placeholder: "@channelname",
        error,
        required: true,
        value: channelHandle
      },
      {
        value: ($$value) => {
          channelHandle = $$value;
          $$settled = false;
        }
      },
      {}
    )} <div><label class="block text-sm font-medium text-gray-700 mb-1" data-svelte-h="svelte-ygt2u5">Number of Videos</label> <input type="range" min="5" max="20" step="1" class="w-full"${add_attribute("value", numVideos, 0)}> <p class="text-sm text-gray-500 mt-1">Using ${escape(numVideos)} videos</p></div> ${validate_component(Button, "Button").$$render($$result, { type: "submit", disabled: loading }, {}, {
      default: () => {
        return `${escape("Start Training")}`;
      }
    })}</form></div>`;
  } while (!$$settled);
  return $$rendered;
});
export {
  Page as default
};
