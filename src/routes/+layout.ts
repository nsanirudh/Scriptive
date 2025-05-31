import { handleAuth } from '../hooks.client';
import type { LayoutLoad } from './$types';

export const load: LayoutLoad = async ({ data }) => {
	const { supabase, session } = await handleAuth();
	
	return { supabase, session };
};