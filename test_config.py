from customer_support_automation.config import settings


print("Application:", settings.app_name)

print("Debug mode:", settings.debug)

print("Database:", settings.database_url)

print("AI key loaded:", bool(settings.ai_api_key))