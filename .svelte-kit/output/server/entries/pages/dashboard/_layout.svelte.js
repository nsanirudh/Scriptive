import { c as create_ssr_component, v as validate_component, a as subscribe, d as each, f as add_attribute, e as escape, m as missing_component } from "../../../chunks/ssr.js";
import { p as page } from "../../../chunks/stores.js";
import "../../../chunks/client.js";
import { clsx } from "clsx";
import { I as Icon } from "../../../chunks/Icon.js";
const Brain = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  const iconNode = [
    [
      "path",
      {
        "d": "M9.5 2A2.5 2.5 0 0 1 12 4.5v15a2.5 2.5 0 0 1-4.96.44 2.5 2.5 0 0 1-2.96-3.08 3 3 0 0 1-.34-5.58 2.5 2.5 0 0 1 1.32-4.24 2.5 2.5 0 0 1 1.98-3A2.5 2.5 0 0 1 9.5 2Z"
      }
    ],
    [
      "path",
      {
        "d": "M14.5 2A2.5 2.5 0 0 0 12 4.5v15a2.5 2.5 0 0 0 4.96.44 2.5 2.5 0 0 0 2.96-3.08 3 3 0 0 0 .34-5.58 2.5 2.5 0 0 0-1.32-4.24 2.5 2.5 0 0 0-1.98-3A2.5 2.5 0 0 0 14.5 2Z"
      }
    ]
  ];
  return `${validate_component(Icon, "Icon").$$render($$result, Object.assign({}, { name: "brain" }, $$props, { iconNode }), {}, {
    default: () => {
      return `${slots.default ? slots.default({}) : ``}`;
    }
  })}`;
});
const File_text = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  const iconNode = [
    [
      "path",
      {
        "d": "M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7.5L14.5 2z"
      }
    ],
    ["polyline", { "points": "14 2 14 8 20 8" }],
    [
      "line",
      {
        "x1": "16",
        "x2": "8",
        "y1": "13",
        "y2": "13"
      }
    ],
    [
      "line",
      {
        "x1": "16",
        "x2": "8",
        "y1": "17",
        "y2": "17"
      }
    ],
    [
      "line",
      {
        "x1": "10",
        "x2": "8",
        "y1": "9",
        "y2": "9"
      }
    ]
  ];
  return `${validate_component(Icon, "Icon").$$render($$result, Object.assign({}, { name: "file-text" }, $$props, { iconNode }), {}, {
    default: () => {
      return `${slots.default ? slots.default({}) : ``}`;
    }
  })}`;
});
const Log_out = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  const iconNode = [
    [
      "path",
      {
        "d": "M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"
      }
    ],
    ["polyline", { "points": "16 17 21 12 16 7" }],
    [
      "line",
      {
        "x1": "21",
        "x2": "9",
        "y1": "12",
        "y2": "12"
      }
    ]
  ];
  return `${validate_component(Icon, "Icon").$$render($$result, Object.assign({}, { name: "log-out" }, $$props, { iconNode }), {}, {
    default: () => {
      return `${slots.default ? slots.default({}) : ``}`;
    }
  })}`;
});
const Layout = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  let $page, $$unsubscribe_page;
  $$unsubscribe_page = subscribe(page, (value) => $page = value);
  const navigation = [
    {
      href: "/dashboard/train",
      label: "Train",
      icon: Brain
    },
    {
      href: "/dashboard/predict",
      label: "Predict",
      icon: File_text
    }
  ];
  $$unsubscribe_page();
  return `<div class="min-h-screen bg-gray-50"><nav class="bg-white shadow"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="flex justify-between h-16"><div class="flex"><div class="flex-shrink-0 flex items-center" data-svelte-h="svelte-177vs78"><span class="text-xl font-bold text-primary">Scriptive</span></div> <div class="hidden sm:ml-6 sm:flex sm:space-x-8">${each(navigation, (item) => {
    return `<a${add_attribute("href", item.href, 0)}${add_attribute(
      "class",
      clsx("inline-flex items-center px-1 pt-1 text-sm font-medium", $page.url.pathname === item.href ? "border-b-2 border-primary text-gray-900" : "text-gray-500 hover:border-b-2 hover:border-gray-300 hover:text-gray-700"),
      0
    )}>${validate_component(item.icon || missing_component, "svelte:component").$$render($$result, { class: "w-4 h-4 mr-2" }, {}, {})} ${escape(item.label)} </a>`;
  })}</div></div> <div class="flex items-center"><button class="inline-flex items-center px-3 py-2 border border-transparent text-sm font-medium rounded-md text-gray-500 hover:text-gray-700">${validate_component(Log_out, "LogOut").$$render($$result, { class: "w-4 h-4 mr-2" }, {}, {})}
            Sign Out</button></div></div></div></nav> <main class="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">${slots.default ? slots.default({}) : ``}</main></div>`;
});
export {
  Layout as default
};
