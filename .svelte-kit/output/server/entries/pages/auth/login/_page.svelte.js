import { c as create_ssr_component, v as validate_component, e as escape } from "../../../../chunks/ssr.js";
import "../../../../chunks/client.js";
import { B as Button } from "../../../../chunks/Button.js";
import { I as Input } from "../../../../chunks/Input.js";
import { I as Icon } from "../../../../chunks/Icon.js";
const Mail = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  const iconNode = [
    [
      "rect",
      {
        "width": "20",
        "height": "16",
        "x": "2",
        "y": "4",
        "rx": "2"
      }
    ],
    [
      "path",
      {
        "d": "m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"
      }
    ]
  ];
  return `${validate_component(Icon, "Icon").$$render($$result, Object.assign({}, { name: "mail" }, $$props, { iconNode }), {}, {
    default: () => {
      return `${slots.default ? slots.default({}) : ``}`;
    }
  })}`;
});
const Page = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  let email = "";
  let password = "";
  let loading = false;
  let error = null;
  let $$settled;
  let $$rendered;
  let previous_head = $$result.head;
  do {
    $$settled = true;
    $$result.head = previous_head;
    $$rendered = `<main class="min-h-screen flex items-center justify-center bg-gray-50"><div class="max-w-md w-full px-6 py-8 bg-white rounded-xl shadow-lg"><div class="flex justify-center mb-8">${validate_component(Mail, "Mail").$$render($$result, { class: "w-12 h-12 text-primary" }, {}, {})}</div> <h1 class="text-3xl font-bold text-center mb-8" data-svelte-h="svelte-lo9zke">Sign In</h1> <form class="space-y-6">${validate_component(Input, "Input").$$render(
      $$result,
      {
        type: "email",
        label: "Email",
        placeholder: "Enter your email",
        error,
        required: true,
        value: email
      },
      {
        value: ($$value) => {
          email = $$value;
          $$settled = false;
        }
      },
      {}
    )} ${validate_component(Input, "Input").$$render(
      $$result,
      {
        type: "password",
        label: "Password",
        placeholder: "Enter your password",
        required: true,
        value: password
      },
      {
        value: ($$value) => {
          password = $$value;
          $$settled = false;
        }
      },
      {}
    )} ${validate_component(Button, "Button").$$render(
      $$result,
      {
        type: "submit",
        class: "w-full",
        disabled: loading
      },
      {},
      {
        default: () => {
          return `${escape("Sign In")}`;
        }
      }
    )}</form></div></main>`;
  } while (!$$settled);
  return $$rendered;
});
export {
  Page as default
};
