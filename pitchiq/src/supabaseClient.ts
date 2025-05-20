// supabaseClient.ts
import { createClient } from '@supabase/supabase-js';

const supabaseUrl = 'https://rcrngkqsybnjfgyvhnyu.supabase.co';
const supabaseAnonKey = '';

export const supabase = createClient(supabaseUrl, supabaseAnonKey);
