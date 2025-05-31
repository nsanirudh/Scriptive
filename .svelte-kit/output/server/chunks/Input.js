import { c as create_ssr_component, i as compute_rest_props, e as escape, j as spread, l as escape_attribute_value, k as escape_object, o as compute_slots } from "./ssr.js";
import { clsx } from "clsx";
const Input = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  let className;
  let $$restProps = compute_rest_props($$props, ["label", "error", "type", "value", "placeholder", "disabled"]);
  let $$slots = compute_slots(slots);
  let { label = void 0 } = $$props;
  let { error = void 0 } = $$props;
  let { type = "text" } = $$props;
  let { value = "" } = $$props;
  let { placeholder = "" } = $$props;
  let { disabled = false } = $$props;
  if ($$props.label === void 0 && $$bindings.label && label !== void 0) $$bindings.label(label);
  if ($$props.error === void 0 && $$bindings.error && error !== void 0) $$bindings.error(error);
  if ($$props.type === void 0 && $$bindings.type && type !== void 0) $$bindings.type(type);
  if ($$props.value === void 0 && $$bindings.value && value !== void 0) $$bindings.value(value);
  if ($$props.placeholder === void 0 && $$bindings.placeholder && placeholder !== void 0) $$bindings.placeholder(placeholder);
  if ($$props.disabled === void 0 && $$bindings.disabled && disabled !== void 0) $$bindings.disabled(disabled);
  className = clsx(
    "w-full px-4 py-2 rounded-lg border bg-white transition-colors",
    error ? "border-red-500 focus:border-red-500" : "border-gray-300 focus:border-primary",
    "focus:outline-none focus:ring-2",
    error ? "focus:ring-red-500/50" : "focus:ring-primary/50",
    "disabled:opacity-50 disabled:cursor-not-allowed",
    $$props.class
  );
  return `${label ? `<label class="block text-sm font-medium text-gray-700 mb-1">${escape(label)}</label>` : ``} <input${spread(
    [
      { type: escape_attribute_value(type) },
      { value: escape_attribute_value(value) },
      {
        placeholder: escape_attribute_value(placeholder)
      },
      { disabled: disabled || null },
      { class: escape_attribute_value(className) },
      {
        "aria-invalid": escape_attribute_value(!!error)
      },
      {
        "aria-errormessage": escape_attribute_value(error ? `error-${$$slots.default}` : void 0)
      },
      escape_object($$restProps)
    ],
    {}
  )}> ${error ? `<p class="mt-1 text-sm text-red-500" id="${"error-" + escape($$slots.default, true)}">${escape(error)}</p>` : ``}`;
});
export {
  Input as I
};
