const groupSelect = document.getElementById("group-select");
const groupDetails = document.getElementById("group-details");
const groupName = document.getElementById("group-name");
const groupOpenings = document.getElementById("group-openings");
const groupPay = document.getElementById("group-pay");
const statusText = document.getElementById("status");

function formatNumber(value) {
	if (value === null || value === undefined) {
		return "N/A";
	}
	return Number(value).toLocaleString();
}

function formatCurrency(value) {
	if (value === null || value === undefined) {
		return "N/A";
	}
	return new Intl.NumberFormat("en-US", {
		style: "currency",
		currency: "USD",
		maximumFractionDigits: 0,
	}).format(value);
}

async function loadGroups() {
	try {
		statusText.textContent = "Loading job groups...";
		const response = await fetch("/groups");

		if (!response.ok) {
			throw new Error("Failed to load groups");
		}

		const groups = await response.json();
		groupSelect.innerHTML = '<option value="">Select a job group</option>';

		groups.forEach((group) => {
			const option = document.createElement("option");
			option.value = group.job_group;
			option.textContent = group.job_group;
			groupSelect.appendChild(option);
		});

		statusText.textContent = "";
	} catch (error) {
		groupSelect.innerHTML = '<option value="">Unable to load groups</option>';
		statusText.textContent = "Could not load job groups. Please try again.";
	}
}

async function loadGroupDetails(jobGroup) {
	if (!jobGroup) {
		groupDetails.hidden = true;
		statusText.textContent = "";
		return;
	}

	try {
		statusText.textContent = "Loading selected group details...";
		const encoded = encodeURIComponent(jobGroup);
		const response = await fetch(`/group/${encoded}`);

		if (!response.ok) {
			throw new Error("Failed to load group details");
		}

		const group = await response.json();
		groupName.textContent = group.job_group;
		groupOpenings.textContent = formatNumber(group.annual_openings);
		groupPay.textContent = formatCurrency(group.med_annual_pay);
		groupDetails.hidden = false;
		statusText.textContent = "";
	} catch (error) {
		groupDetails.hidden = true;
		statusText.textContent = "Could not load details for this group.";
	}
}

groupSelect.addEventListener("change", (event) => {
	loadGroupDetails(event.target.value);
});

loadGroups();
