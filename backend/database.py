from supabase import create_client
import os


url=os.getenv(
    "https://vphijxurezcpvzkmnjfn.supabase.co/rest/v1/"
)

key=os.getenv(
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZwaGlqeHVyZXpjcHZ6a21uamZuIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODYwNjAwODYsImV4cCI6MjEwMTYzNjA4Nn0.2sUAOauLfamSwRhjNGQfxcoSwWcYQUQrzMUq_TXIgoI"
)


supabase=create_client(
    url,
    key
)