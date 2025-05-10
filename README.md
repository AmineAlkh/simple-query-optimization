# Simple Query Optimization Task

## Task Description

The API endpoint at `/api/order-item/`, managed by the `OrderItemViewSet`, is currently experiencing poor performance, with response times around **5 seconds**.

**Objective:**
Optimize the performance of this endpoint to reduce response time to **200ms** or less.

You are free to make any necessary changes to achieve this goal.
Please include a short description of any changes or optimizations you make in a file named `description.md`.

Please respond to the email with a link to a GitLab or GitHub repository containing your completed solution.

## How to Run the Project

```bash
# Start the project
docker compose up -d

# Apply database migrations
docker compose exec fred python manage.py migrate

# Populate the database with sample data
docker compose exec fred python manage.py generate_data --users 20 --products 400 --orders 1000 --orderitems 4000

# The endpoint should now be accessible at http://localhost:8000/api/order-item/  
```
Note: Of course, you can run the project as you like (without Docker). Running by Docker is just for simplicity when running the project for the first time.


