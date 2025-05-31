import { c as create_ssr_component, f as add_attribute } from "./ssr.js";
import { clsx } from "clsx";
const Button = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  let className;
  let { variant = "primary" } = $$props;
  let { size = "md" } = $$props;
  let { type = "button" } = $$props;
  let { disabled = false } = $$props;
  const variants = {
    primary: "bg-primary text-white hover:bg-primary/90",
    secondary: "bg-secondary text-white hover:bg-secondary/90",
    outline: "border-2 border-primary text-primary hover:bg-primary/10"
  };
  const sizes = {
    sm: "px-3 py-1.5 text-sm",
    md: "px-4 py-2",
    lg: "px-6 py-3 text-lg"
  };
  if ($$props.variant === void 0 && $$bindings.variant && variant !== void 0) $$bindings.variant(variant);
  if ($$props.size === void 0 && $$bindings.size && size !== void 0) $$bindings.size(size);
  if ($$props.type === void 0 && $$bindings.type && type !== void 0) $$bindings.type(type);
  if ($$props.disabled === void 0 && $$bindings.disabled && disabled !== void 0) $$bindings.disabled(disabled);
  className = clsx("rounded-lg font-medium transition-colors focus:outline-none focus:ring-2 focus:ring-primary/50 disabled:opacity-50 disabled:cursor-not-allowed", variants[variant], sizes[size], $$props.class);
  return `<button${add_attribute("type", type, 0)} ${disabled ? "disabled" : ""}${add_attribute("class", className, 0)}>${slots.default ? slots.default({}) : ``}</button>`;
});
export {
  Button as B
};
