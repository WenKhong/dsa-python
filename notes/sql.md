# SQL Notes — Clinic Data

Practice queries on a simple clinic booking schema (PostgreSQL / Supabase).

## Schema

```sql
patients     (id, name, phone, created_at)
services     (id, name, price)
appointments (id, patient_id, service_id, appointment_date, status)
-- status: 'booked' | 'completed' | 'cancelled' | 'no_show'
```

---

## 1. Which services are booked most?

```sql
SELECT s.name AS service,
       COUNT(a.id) AS bookings
FROM appointments a
JOIN services s ON s.id = a.service_id
WHERE a.status <> 'cancelled'
GROUP BY s.id, s.name
ORDER BY bookings DESC;
```

**Concepts:** `JOIN`, `GROUP BY`, `COUNT`, `ORDER BY ... DESC`
**Why it matters:** Shows which services drive demand, so the clinic knows which to promote and staff for.

---

## 2. Which services have the highest no-show rate?

```sql
SELECT s.name AS service,
       COUNT(*) AS due_appointments,
       SUM(CASE WHEN a.status = 'no_show' THEN 1 ELSE 0 END) AS no_shows,
       ROUND(100.0 * SUM(CASE WHEN a.status = 'no_show' THEN 1 ELSE 0 END)
             / COUNT(*), 1) AS no_show_pct
FROM appointments a
JOIN services s ON s.id = a.service_id
WHERE a.status IN ('completed', 'no_show')
GROUP BY s.id, s.name
ORDER BY no_show_pct DESC;
```

**Concepts:** conditional aggregation (`SUM(CASE WHEN ...)`), `100.0` to force decimal division, `ROUND`
**Why it matters:** No-shows are lost revenue. This shows which services need stronger reminders (e.g. a WhatsApp reminder 24h before).

---

## 3. Which patients haven't visited in 6+ months?

```sql
SELECT p.name,
       p.phone,
       MAX(a.appointment_date) AS last_visit
FROM patients p
JOIN appointments a ON a.patient_id = p.id
WHERE a.status = 'completed'
GROUP BY p.id, p.name, p.phone
HAVING MAX(a.appointment_date) < CURRENT_DATE - INTERVAL '6 months'
ORDER BY last_visit;
```

**Concepts:** `MAX` per group, `HAVING` (filters groups, while `WHERE` filters rows), date arithmetic
**Why it matters:** This is the recall list for win-back campaigns, a direct revenue lever for the clinic.