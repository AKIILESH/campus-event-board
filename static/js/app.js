document.addEventListener('DOMContentLoaded', () => {
  let allEvents = [];
  let currentCategory = 'all';
  let searchQuery = '';

  const eventsContainer = document.getElementById('eventsContainer');
  const searchInput = document.getElementById('searchInput');
  const categoryChips = document.querySelectorAll('.chip');
  const regModal = document.getElementById('regModal');
  const ticketModal = document.getElementById('ticketModal');
  const regForm = document.getElementById('regForm');
  const myTicketsModal = document.getElementById('myTicketsModal');

  // Load events initially
  fetchEvents();

  // Search input handler
  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      searchQuery = e.target.value.toLowerCase();
      renderEvents();
    });
  }

  // Category chips filter
  categoryChips.forEach(chip => {
    chip.addEventListener('click', () => {
      categoryChips.forEach(c => c.classList.remove('active'));
      chip.classList.add('active');
      currentCategory = chip.dataset.category;
      renderEvents();
    });
  });

  // Modal close buttons
  document.querySelectorAll('[data-close-modal]').forEach(btn => {
    btn.addEventListener('click', (e) => {
      const modal = e.target.closest('.modal-overlay');
      if (modal) modal.classList.remove('active');
    });
  });

  // Fetch events from Flask backend
  async function fetchEvents() {
    renderSkeletons();
    try {
      const res = await fetch('/api/events');
      allEvents = await res.json();
      updateHeroStats(allEvents);
      renderEvents();
    } catch (err) {
      console.error('Failed to load events:', err);
      eventsContainer.innerHTML = `
        <div style="grid-column: 1/-1; text-align: center; padding: 3rem; color: var(--accent-rose);">
          <i class="fa-solid fa-triangle-exclamation" style="font-size: 2.5rem; margin-bottom: 1rem;"></i>
          <p>Failed to load campus events. Please check the backend connection.</p>
        </div>
      `;
    }
  }

  function updateHeroStats(events) {
    const totalEventsEl = document.getElementById('statTotalEvents');
    const totalRegEl = document.getElementById('statTotalReg');
    const totalOpenEl = document.getElementById('statTotalOpen');

    if (totalEventsEl) totalEventsEl.textContent = events.length;
    if (totalRegEl) {
      const regCount = events.reduce((sum, ev) => sum + (ev.registered_count || 0), 0);
      totalRegEl.textContent = regCount;
    }
    if (totalOpenEl) {
      const openCount = events.filter(ev => ev.status === 'Open').length;
      totalOpenEl.textContent = openCount;
    }
  }

  function renderSkeletons() {
    if (!eventsContainer) return;
    eventsContainer.innerHTML = Array(6).fill(0).map(() => `
      <div class="skeleton skeleton-card"></div>
    `).join('');
  }

  function renderEvents() {
    if (!eventsContainer) return;

    const filtered = allEvents.filter(ev => {
      const matchCat = currentCategory === 'all' || ev.category.toLowerCase() === currentCategory.toLowerCase();
      const matchSearch = !searchQuery || 
        ev.title.toLowerCase().includes(searchQuery) ||
        ev.venue.toLowerCase().includes(searchQuery) ||
        ev.organizer.toLowerCase().includes(searchQuery) ||
        (ev.description && ev.description.toLowerCase().includes(searchQuery));
      return matchCat && matchSearch;
    });

    if (filtered.length === 0) {
      eventsContainer.innerHTML = `
        <div style="grid-column: 1/-1; text-align: center; padding: 4rem 1rem; color: var(--text-secondary);">
          <i class="fa-solid fa-calendar-xmark" style="font-size: 3rem; margin-bottom: 1rem; color: var(--text-muted);"></i>
          <h3>No matching events found</h3>
          <p style="font-size: 0.9rem; margin-top: 0.5rem;">Try adjusting your search query or switching categories.</p>
        </div>
      `;
      return;
    }

    eventsContainer.innerHTML = filtered.map(ev => {
      const isFull = ev.registered_count >= ev.capacity;
      const isOpen = ev.status === 'Open' && !isFull;
      const percent = Math.min(100, Math.round((ev.registered_count / ev.capacity) * 100));

      return `
        <div class="event-card">
          <div class="card-top">
            <span class="category-tag">
              <i class="fa-solid ${getCategoryIcon(ev.category)}"></i>
              ${escapeHtml(ev.category)}
            </span>
            <span class="status-pill ${isOpen ? 'status-open' : 'status-closed'}">
              <i class="fa-solid ${isOpen ? 'fa-circle-check' : 'fa-lock'}"></i>
              ${isOpen ? 'Open' : (isFull ? 'Full' : 'Closed')}
            </span>
          </div>

          <h3 class="event-title">${escapeHtml(ev.title)}</h3>
          
          <div class="event-organizer">
            <i class="fa-solid fa-user-tie"></i>
            <span>${escapeHtml(ev.organizer)}</span>
          </div>

          <div class="event-meta">
            <div class="meta-item">
              <i class="fa-regular fa-calendar-days"></i>
              <span>${escapeHtml(ev.event_date)}</span>
            </div>
            <div class="meta-item">
              <i class="fa-regular fa-clock"></i>
              <span>${escapeHtml(ev.event_time)}</span>
            </div>
            <div class="meta-item" style="grid-column: 1 / -1;">
              <i class="fa-solid fa-location-dot"></i>
              <span>${escapeHtml(ev.venue)}</span>
            </div>
          </div>

          <p class="event-desc">${escapeHtml(ev.description || 'Join this exciting campus event!')}</p>

          <div class="capacity-tracker">
            <div class="capacity-label">
              <span>Registrations</span>
              <span><strong>${ev.registered_count}</strong> / ${ev.capacity} Seats (${percent}%)</span>
            </div>
            <div class="progress-bg">
              <div class="progress-fill" style="width: ${percent}%;"></div>
            </div>
          </div>

          <div class="card-footer">
            ${isOpen ? `
              <button class="btn btn-primary" style="width: 100%;" onclick="openRegisterModal(${ev.id})">
                <i class="fa-solid fa-ticket"></i> Register Now
              </button>
            ` : `
              <button class="btn btn-secondary" style="width: 100%; cursor: not-allowed; opacity: 0.6;" disabled>
                <i class="fa-solid fa-ban"></i> Registrations Closed
              </button>
            `}
          </div>
        </div>
      `;
    }).join('');
  }

  function getCategoryIcon(cat) {
    const map = {
      'hackathon': 'fa-code',
      'workshop': 'fa-laptop-code',
      'cultural': 'fa-masks-theater',
      'technical': 'fa-microchip',
      'sports': 'fa-volleyball',
      'seminar': 'fa-graduation-cap'
    };
    return map[cat.toLowerCase()] || 'fa-calendar-check';
  }

  window.openRegisterModal = function(eventId) {
    const event = allEvents.find(e => e.id === eventId);
    if (!event) return;

    document.getElementById('regEventId').value = event.id;
    document.getElementById('modalEventTitle').textContent = event.title;
    document.getElementById('modalEventSub').textContent = `${event.category} • ${event.event_date} at ${event.event_time}`;
    document.getElementById('modalEventVenue').textContent = event.venue;

    // Reset error
    const errBox = document.getElementById('regErrorMsg');
    if (errBox) errBox.style.display = 'none';

    regModal.classList.add('active');
  };

  // Handle registration submit
  if (regForm) {
    regForm.addEventListener('submit', async (e) => {
      e.preventDefault();
      const submitBtn = regForm.querySelector('button[type="submit"]');
      const originalText = submitBtn.innerHTML;
      submitBtn.disabled = true;
      submitBtn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Registering...';

      const payload = {
        event_id: parseInt(document.getElementById('regEventId').value),
        student_name: document.getElementById('studentName').value,
        roll_no: document.getElementById('rollNo').value,
        department: document.getElementById('department').value,
        year: document.getElementById('year').value,
        email: document.getElementById('email').value,
        phone: document.getElementById('phone').value
      };

      try {
        const res = await fetch('/api/register', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(payload)
        });

        const data = await res.json();

        if (res.ok && data.success) {
          regModal.classList.remove('active');
          regForm.reset();
          
          // Save ticket to localStorage
          saveLocalTicket(data);
          
          // Show ticket pass
          showTicketModal(data);

          // Refresh events count
          fetchEvents();
        } else {
          const errBox = document.getElementById('regErrorMsg');
          if (errBox) {
            errBox.textContent = data.error || 'Failed to submit registration.';
            errBox.style.display = 'block';
          }
        }
      } catch (err) {
        console.error('Registration error:', err);
        const errBox = document.getElementById('regErrorMsg');
        if (errBox) {
          errBox.textContent = 'Network or server error. Please try again.';
          errBox.style.display = 'block';
        }
      } finally {
        submitBtn.disabled = false;
        submitBtn.innerHTML = originalText;
      }
    });
  }

  function showTicketModal(ticket) {
    document.getElementById('passCode').textContent = ticket.ticket_code;
    document.getElementById('passEvent').textContent = ticket.event_title;
    document.getElementById('passStudent').textContent = ticket.student_name;
    document.getElementById('passRoll').textContent = ticket.roll_no;
    document.getElementById('passDate').textContent = `${ticket.event_date} (${ticket.event_time})`;
    document.getElementById('passVenue').textContent = ticket.venue;

    ticketModal.classList.add('active');
  }

  function saveLocalTicket(ticket) {
    try {
      const tickets = JSON.parse(localStorage.getItem('cit_event_tickets') || '[]');
      tickets.unshift({
        ...ticket,
        saved_at: new Date().toISOString()
      });
      localStorage.setItem('cit_event_tickets', JSON.stringify(tickets));
    } catch (e) {
      console.warn('Could not save to localStorage', e);
    }
  }

  // My tickets button handler
  const myTicketsBtn = document.getElementById('myTicketsBtn');
  if (myTicketsBtn) {
    myTicketsBtn.addEventListener('click', () => {
      renderMyTickets();
      myTicketsModal.classList.add('active');
    });
  }

  function renderMyTickets() {
    const listEl = document.getElementById('myTicketsList');
    if (!listEl) return;
    const tickets = JSON.parse(localStorage.getItem('cit_event_tickets') || '[]');

    if (tickets.length === 0) {
      listEl.innerHTML = `
        <div style="text-align: center; padding: 2rem; color: var(--text-secondary);">
          <i class="fa-solid fa-ticket-simple" style="font-size: 2rem; margin-bottom: 0.5rem; color: var(--text-muted);"></i>
          <p>No event passes found on this device.</p>
        </div>
      `;
      return;
    }

    listEl.innerHTML = tickets.map(t => `
      <div style="background: rgba(255,255,255,0.03); border: 1px solid var(--border-color); border-radius: var(--radius-md); padding: 1rem; margin-bottom: 0.75rem;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
          <strong style="color: var(--primary); font-family: monospace;">${escapeHtml(t.ticket_code)}</strong>
          <span style="font-size: 0.75rem; color: var(--text-muted);">${escapeHtml(t.roll_no)}</span>
        </div>
        <h4 style="font-size: 1rem; margin-bottom: 0.25rem;">${escapeHtml(t.event_title)}</h4>
        <p style="font-size: 0.8rem; color: var(--text-secondary);"><i class="fa-regular fa-calendar"></i> ${escapeHtml(t.event_date)} • ${escapeHtml(t.venue)}</p>
      </div>
    `).join('');
  }

  function escapeHtml(str) {
    if (!str) return '';
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#039;');
  }
});
