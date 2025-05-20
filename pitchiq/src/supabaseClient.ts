// supabaseClient.ts
import { createClient } from '@supabase/supabase-js';

const supabaseUrl = 'https://rcrngkqsybnjfgyvhnyu.supabase.co';
const supabaseAnonKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJjcm5na3FzeWJuamZneXZobnl1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDY5OTYxMzAsImV4cCI6MjA2MjU3MjEzMH0.cMqEN71x059wG5Gw0oDgDk5N8FJ1fgOpTiJ4SP3ppEw';

export const supabase = createClient(supabaseUrl, supabaseAnonKey);
