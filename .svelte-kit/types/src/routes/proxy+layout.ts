// @ts-nocheck
import { handleAuth } from '../hooks.client';
import type { LayoutLoad } from './$types';

export const load = async ({ data }: Parameters<LayoutLoad>[0]) => {
	const { supabase, session } = await handleAuth();
	
	return { supabase, session };
};