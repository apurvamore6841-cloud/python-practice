# Take amount from the user
amount = float(input("Enter amount: "))

# Calculate 18 percent GST
gst = amount * 18 / 100
# Add GST to the original amount
final_amount = amount + gst

# Display GST amount
print(f"GST: {gst:.2f}")
print(f"Final amount:{final_amount:.2f}")