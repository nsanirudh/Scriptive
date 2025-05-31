import { c as create_ssr_component, v as validate_component, h as createEventDispatcher, f as add_attribute, e as escape, d as each } from "../../../../chunks/ssr.js";
import { B as Button } from "../../../../chunks/Button.js";
import { I as Input } from "../../../../chunks/Input.js";
import { clsx } from "clsx";
import { I as Icon } from "../../../../chunks/Icon.js";
const Upload = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  const iconNode = [
    [
      "path",
      {
        "d": "M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"
      }
    ],
    ["polyline", { "points": "17 8 12 3 7 8" }],
    [
      "line",
      {
        "x1": "12",
        "x2": "12",
        "y1": "3",
        "y2": "15"
      }
    ]
  ];
  return `${validate_component(Icon, "Icon").$$render($$result, Object.assign({}, { name: "upload" }, $$props, { iconNode }), {}, {
    default: () => {
      return `${slots.default ? slots.default({}) : ``}`;
    }
  })}`;
});
const FileUpload = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  let { multiple = false } = $$props;
  let { accept = "*" } = $$props;
  let { error = void 0 } = $$props;
  createEventDispatcher();
  if ($$props.multiple === void 0 && $$bindings.multiple && multiple !== void 0) $$bindings.multiple(multiple);
  if ($$props.accept === void 0 && $$bindings.accept && accept !== void 0) $$bindings.accept(accept);
  if ($$props.error === void 0 && $$bindings.error && error !== void 0) $$bindings.error(error);
  return `<div${add_attribute(
    "class",
    clsx(
      "border-2 border-dashed rounded-lg p-8 text-center transition-colors",
      "border-gray-300",
      "hover:border-primary hover:bg-primary/5",
      error && "border-red-500 hover:border-red-500"
    ),
    0
  )}><input type="file" ${multiple ? "multiple" : ""}${add_attribute("accept", accept, 0)} class="hidden"> ${validate_component(Upload, "Upload").$$render(
    $$result,
    {
      class: "w-12 h-12 mx-auto mb-4 text-gray-400"
    },
    {},
    {}
  )} <p class="text-sm text-gray-600 mb-2">Drag and drop your files here, or
    <button type="button" class="text-primary hover:underline" data-svelte-h="svelte-1isi9nd">browse</button></p> ${error ? `<p class="text-sm text-red-500 mt-2">${escape(error)}</p>` : ``}</div>`;
});
const Page = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  let channelId = "";
  let topic = "";
  let loading = false;
  let error = null;
  const tones = ["educational", "dramatic", "casual", "professional"];
  const audiences = ["general", "beginners", "intermediate", "advanced"];
  const lengths = ["short", "medium", "long"];
  let $$settled;
  let $$rendered;
  let previous_head = $$result.head;
  do {
    $$settled = true;
    $$result.head = previous_head;
    $$rendered = `<div class="bg-white shadow rounded-lg p-6"><h1 class="text-2xl font-bold mb-6" data-svelte-h="svelte-aets2a">Generate Script</h1> <form class="space-y-6"><div class="grid grid-cols-1 md:grid-cols-2 gap-6">${validate_component(Input, "Input").$$render(
      $$result,
      {
        type: "text",
        label: "Channel ID",
        placeholder: "Enter the ID of a trained channel (e.g., veritasium)",
        required: true,
        value: channelId
      },
      {
        value: ($$value) => {
          channelId = $$value;
          $$settled = false;
        }
      },
      {
        default: () => {
          return `<p class="mt-1 text-sm text-gray-500" data-svelte-h="svelte-yw65cf">This is the ID of a channel you&#39;ve already trained in the Train tab. The generated script will mimic this channel&#39;s style.</p>`;
        }
      }
    )} ${validate_component(Input, "Input").$$render(
      $$result,
      {
        type: "text",
        label: "Topic",
        placeholder: "What's your video about?",
        required: true,
        value: topic
      },
      {
        value: ($$value) => {
          topic = $$value;
          $$settled = false;
        }
      },
      {}
    )} <div><label class="block text-sm font-medium text-gray-700 mb-1" data-svelte-h="svelte-16xyoyz">Tone</label> <select class="w-full px-4 py-2 rounded-lg border border-gray-300 focus:border-primary focus:outline-none focus:ring-2 focus:ring-primary/50">${each(tones, (t) => {
      return `<option${add_attribute("value", t, 0)}>${escape(t)}</option>`;
    })}</select></div> <div><label class="block text-sm font-medium text-gray-700 mb-1" data-svelte-h="svelte-1uhj9im">Target Audience</label> <select class="w-full px-4 py-2 rounded-lg border border-gray-300 focus:border-primary focus:outline-none focus:ring-2 focus:ring-primary/50">${each(audiences, (a) => {
      return `<option${add_attribute("value", a, 0)}>${escape(a)}</option>`;
    })}</select></div> <div><label class="block text-sm font-medium text-gray-700 mb-1" data-svelte-h="svelte-t5fsa7">Length</label> <select class="w-full px-4 py-2 rounded-lg border border-gray-300 focus:border-primary focus:outline-none focus:ring-2 focus:ring-primary/50">${each(lengths, (l) => {
      return `<option${add_attribute("value", l, 0)}>${escape(l)}</option>`;
    })}</select></div></div> <div><label class="block text-sm font-medium text-gray-700 mb-1" data-svelte-h="svelte-unwvat">Reference Documents (Optional)</label> ${validate_component(FileUpload, "FileUpload").$$render(
      $$result,
      {
        multiple: true,
        accept: ".pdf,.docx,.txt",
        error
      },
      {},
      {}
    )}</div> ${validate_component(Button, "Button").$$render($$result, { type: "submit", disabled: loading }, {}, {
      default: () => {
        return `${escape("Generate Script")}`;
      }
    })}</form> ${``}</div>`;
  } while (!$$settled);
  return $$rendered;
});
export {
  Page as default
};
