/**
 * Highlights current navbar item by comparing URL with href attributes.
 * Applies style classes to the matching item (exact or partial match).
 */
export const activateCurrentNavbarItem = () => {
  const urlPath = window.location.pathname;
  const navbarItems = document.querySelectorAll(".navbar-item[href]");

  for (const navbarItem of navbarItems) {
    const href = navbarItem.getAttribute("href");

    const isExactMatch = urlPath === href;
    const isPartialMatch = urlPath.startsWith(href) && href !== "/";

    if (!isExactMatch && !isPartialMatch) continue;

    navbarItem.classList.add("has-background-link-light", "has-text-link-dark");
    break;
  }
};

/**
 * Toggles navbar menu visibility when burger icon is clicked.
 * Adds/removes `is-active` class to show or hide the menu.
 */
export const turnOnNavbarMenuToggle = () => {
  const navbarBurgers = document.querySelectorAll(".navbar-burger");

  navbarBurgers.forEach((navbarBurger) => {
    navbarBurger.addEventListener("click", () => {
      const { target } = navbarBurger.dataset;

      navbarBurger.classList.toggle("is-active");
      document.querySelector(target).classList.toggle("is-active");
    });
  });
};

/**
 * Applies IMask to fields with the `data-mask` or `data-regex` attribute.
 */
export const activateIMask = () => {
  const fields = document.querySelectorAll("[data-mask], [data-regex]");

  fields.forEach((field) => {
    const { mask, regex } = field.dataset;
    IMask(field, { mask: mask || new RegExp(regex) });
  });
};

/**
 * Enables/disables submit button based on form field changes.
 * The button activates when any field is modified.
 */
export const turnOnDirtyFormCheck = () => {
  const submitButton = document.querySelector("button[type='submit']");
  if (!submitButton) return;

  const fields = Array.from(
    document.querySelectorAll("input, select, textarea")
  );
  const initialValues = fields.map((field) => field.value);

  fields.forEach((field) => {
    field.addEventListener("input", () => {
      const wasModified = fields.some(
        (curField, curIndex) => curField.value !== initialValues[curIndex]
      );

      if (wasModified) submitButton.removeAttribute("disabled");
      else submitButton.setAttribute("disabled", "true");
    });
  });
};

/**
 * Sets up redirects when clicking table rows with `data-href`.
 * Navigates to the URL specified in the row's href dataset attribute.
 */
export const turnOnTableRowsRedirect = () => {
  const rows = document.querySelectorAll("tr[data-href]");

  rows.forEach((row) => {
    row.addEventListener("click", () => {
      const { href } = row.dataset;
      window.location.href = href;
    });
  });
};

/**
 * Adds fade-out animation to notifications after 3 seconds.
 * Replaces `animate__fadeInRight` with `animate__fadeOutRight` class.
 */
export const activateNotificationFadeOut = () => {
  const notifications = document.querySelectorAll(".notification");

  notifications.forEach((notification) => {
    setTimeout(() => {
      notification.classList.remove("animate__fadeInRight");
      notification.classList.add("animate__fadeOutRight");
    }, 3 * 1000);
  });
};

document.addEventListener("DOMContentLoaded", () => {
  // navbar _
  activateCurrentNavbarItem();
  turnOnNavbarMenuToggle();

  // form _
  activateIMask();
  turnOnDirtyFormCheck();

  // table _
  turnOnTableRowsRedirect();

  // notification _
  activateNotificationFadeOut();
});
