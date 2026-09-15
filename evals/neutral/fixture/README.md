# Repair desk
A local Python 3 standard-library experiment. The overview calls attention_today(requests, today). Dates are valid ISO calendar dates, supplied by the caller in its already selected time zone. There is no database, browser, network service, or deployment adapter in this repository. Input shape stays unchanged; supported status values are open, in_progress, completed, cancelled. due_date is an ISO date or None. Callers rely on input order and input immutability. Tests: python -m unittest discover -v.

The desired meaning of 'needs attention today' has not been agreed: treatment of due-today, undated, in-progress and completed items still needs a business decision. Do not extend into invalid date handling, scheduling, notifications, persistence, or UI.
