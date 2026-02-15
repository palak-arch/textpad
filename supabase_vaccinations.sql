-- Create a table for tracking user vaccinations
create table if not exists public.vaccination_records (
  id uuid default gen_random_uuid() primary key,
  user_id uuid references auth.users(id) on delete cascade not null,
  vaccine_name text not null,
  date_administered date,
  scheduled_date date,
  status text check (status in ('completed', 'scheduled', 'overdue')) default 'scheduled',
  notes text,
  created_at timestamp with time zone default timezone('utc'::text, now()) not null
);

-- Set up Row Level Security (RLS)
alter table public.vaccination_records enable row level security;

-- Policy: Users can view their own records
create policy "Users can view their own vaccination records"
  on public.vaccination_records for select
  using (auth.uid() = user_id);

-- Policy: Users can insert their own records
create policy "Users can insert their own vaccination records"
  on public.vaccination_records for insert
  with check (auth.uid() = user_id);

-- Policy: Users can update their own records
create policy "Users can update their own vaccination records"
  on public.vaccination_records for update
  using (auth.uid() = user_id);

-- Policy: Users can delete their own records
create policy "Users can delete their own vaccination records"
  on public.vaccination_records for delete
  using (auth.uid() = user_id);
