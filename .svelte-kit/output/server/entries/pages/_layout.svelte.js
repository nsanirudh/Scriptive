import { c as create_ssr_component, a as subscribe } from "../../chunks/ssr.js";
import { w as writable } from "../../chunks/index2.js";
import { g as goto } from "../../chunks/client.js";
import { p as page } from "../../chunks/stores.js";
const isAuthenticated = writable(false);
const Layout = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  let $isAuthenticated, $$unsubscribe_isAuthenticated;
  let $page, $$unsubscribe_page;
  $$unsubscribe_isAuthenticated = subscribe(isAuthenticated, (value) => $isAuthenticated = value);
  $$unsubscribe_page = subscribe(page, (value) => $page = value);
  {
    if ($page.url.pathname.startsWith("/dashboard") && !$isAuthenticated) {
      goto();
    }
  }
  $$unsubscribe_isAuthenticated();
  $$unsubscribe_page();
  return `${slots.default ? slots.default({}) : ``}`;
});
export {
  Layout as default
};
