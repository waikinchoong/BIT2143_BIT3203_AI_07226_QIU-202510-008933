# PEAS and Formal AI Problem Formulation

<!-- Fill this in during/after tomorrow's tutorial, using your Part B and Part C answers
     from the Wk3b worksheet. Delete each instruction line once replaced with your own text.
     Everything below Part C is a preview for next week — a first sketch is fine, it does
     not need to be complete for the Concept Check. -->

## PEAS

Performance measure (how success is judged):

Assign charging stations without booking conflicts, satisfy users' preferred time whenever possible, and maximize charging station utilization.

Environment (where the agent operates):

EV owners, charging stations, booking requests, and available time slots.

Actuators (how the agent acts):

Assign charging stations, assign time slots, and display booking results.

Sensors (what the agent perceives):

Booking requests, charging station availability, and available time slots.


## Environment properties

<!-- Worksheet Part C. Circle/decide one option per line — this determines whether
     search or CSP fits your problem, which you'll formalise next week. -->

Observable:

Fully Observable

Deterministic: Yes

Episodic or Sequential:

Sequential

Static or Dynamic:

Static

Discrete or Continuous:

Discrete

## State or variables

<!-- Draft only — refine next week once your method (search vs CSP) is confirmed. -->

Each EV booking is assigned to a charging station and a time slot.


## Initial state

Booking requests are received, and all charging stations and time slots are available before scheduling starts.


## Actions or domains
Available charging stations and available time slots for each booking.

## Transition model or constraints

A charging station cannot be assigned to more than one EV at the same time.
Each booking must be assigned to only one charging station.
Each booking must use one available time slot.
## Goal test
All EV bookings are assigned without scheduling conflicts.

## Path cost
Minimize booking conflicts and maximize charging station utilization.

## Heuristic, where applicable
Not applicable for this initial CSP draft.

---

## Appendix: draft simple reflex agent rules (early sketch, Part D)

<!-- Optional early thinking from the tutorial — condition-action rules, not the final
     algorithm. Keep or delete once your real AI method is decided next week. -->

Rule 1:
If a charging station is available, then assign the booking.

Rule 2:
If the preferred time slot is unavailable, then reject the booking.

Rule 3:
If no charging station is available, then reject the booking.