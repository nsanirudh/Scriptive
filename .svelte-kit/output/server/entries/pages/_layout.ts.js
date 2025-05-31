import { P as PUBLIC_SUPABASE_ANON_KEY, a as PUBLIC_SUPABASE_URL } from "../../chunks/public.js";
import { createSupabaseLoadClient } from "@supabase/auth-helpers-sveltekit";
const handleAuth = async () => {
  const supabase = createSupabaseLoadClient({
    supabaseUrl: PUBLIC_SUPABASE_URL,
    supabaseKey: PUBLIC_SUPABASE_ANON_KEY,
    event: { fetch },
    serverSession: null
  });
  const {
    data: { session }
  } = await supabase.auth.getSession();
  return {
    supabase,
    session
  };
};
const load = async ({ data }) => {
  const { supabase, session } = await handleAuth();
  return { supabase, session };
};
export {
  load
};
