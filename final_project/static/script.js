const groupList = document.getElementById("group-list");
const groupDetails = document.getElementById("group-details");
const groupName = document.getElementById("group-name");
const groupOpenings = document.getElementById("group-openings");
const groupPay = document.getElementById("group-pay");
const jobDetails = document.getElementById("job-details");
const jobName = document.getElementById("job-name");
const jobGroup = document.getElementById("job-group");
const jobOpenings = document.getElementById("job-openings");
const jobPay = document.getElementById("job-pay");
const jobEducation = document.getElementById("job-education");
const statusText = document.getElementById("status");

let activeGroupItem = null;
let activeJobButton = null;

function getGroupEmoji(jobGroup) {
	const name = jobGroup.toLowerCase();

	if (name.includes("architecture") || name.includes("engineering")) return "🏗️";
	if (name.includes("arts") || name.includes("design")) return "🎨";
	if (name.includes("cleaning") || name.includes("grounds")) return "🧹";
	if (name.includes("business") || name.includes("financial")) return "💼";
	if (name.includes("community") || name.includes("social service")) return "🤝";
	if (name.includes("computer") || name.includes("technology")) return "💻";
	if (name.includes("construction") || name.includes("extraction")) return "🏠";
	if (name.includes("educational") || name.includes("library")) return "📚";
	if (name.includes("entertainment") || name.includes("sports")) return "🎭";
	if (name.includes("farming") || name.includes("fishing") || name.includes("forestry")) return "🌾";
	if (name.includes("food") || name.includes("serving")) return "🍽️";
	if (name.includes("healthcare")) return "🩺";
	if (name.includes("maintenance") || name.includes("repair")) return "🛠️";
	if (name.includes("legal")) return "⚖️";
	if (name.includes("science")) return "🔬";
	if (name.includes("management")) return "📈";
	if (name.includes("math")) return "➗";
	if (name.includes("media") || name.includes("communication")) return "📰";
	if (name.includes("administrative") || name.includes("office")) return "🗂️";
	if (name.includes("personal care") || name.includes("service")) return "🧰";
	if (name.includes("production")) return "🏭";
	if (name.includes("protective")) return "🛡️";
	if (name.includes("sales")) return "🛍️";
	if (name.includes("transportation") || name.includes("material moving")) return "🚚";

	return "📌";
}

function withEmoji(jobGroup) {
	return `${jobGroup} ${getGroupEmoji(jobGroup)}`;
}

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
		groupList.innerHTML = "";

		groups.forEach((group) => {
			const item = document.createElement("li");
			item.className = "group-item";

			const trigger = document.createElement("button");
			trigger.type = "button";
			trigger.className = "group-trigger";
			trigger.textContent = withEmoji(group.job_group);
			trigger.addEventListener("click", () => {
				handleGroupClick(group, item);
			});

			item.appendChild(trigger);
			groupList.appendChild(item);
		});

		statusText.textContent = "";
	} catch (error) {
		groupList.innerHTML = "<li>Unable to load groups</li>";
		statusText.textContent = "Could not load job groups. Please try again.";
	}
}

function renderGroupDetails(group) {
	if (!group) {
		groupDetails.hidden = true;
		renderJobDetails(null);
		return;
	}

	groupName.textContent = withEmoji(group.job_group);
	groupOpenings.textContent = formatNumber(group.annual_openings);
	groupPay.textContent = formatCurrency(group.med_annual_pay);
	groupDetails.hidden = false;
}

function renderJobDetails(job) {
	if (!job) {
		jobDetails.hidden = true;
		return;
	}

	jobName.textContent = job.job_name;
	jobGroup.textContent = job.job_group || "N/A";
	jobOpenings.textContent = formatNumber(job.annual_openings);
	jobPay.textContent = formatCurrency(job.med_annual_pay);
	jobEducation.textContent = job.entry_lvl_ed || "N/A";
	jobDetails.hidden = false;
}


async function loadJobsForGroup(jobGroup) {
	try {
		statusText.textContent = "Loading jobs for selected group...";
		const encoded = encodeURIComponent(jobGroup);
		const response = await fetch(`/group/${encoded}/jobs`);

		if (!response.ok) {
			throw new Error("Failed to load jobs");
		}

		const jobs = await response.json();
		statusText.textContent = "";
		return jobs;
	} catch (error) {
		statusText.textContent = "Could not load jobs for this group.";
		return null;
	}
}

async function loadJobDetails(jobNameValue) {
	try {
		statusText.textContent = "Loading selected job details...";
		const encoded = encodeURIComponent(jobNameValue);
		const response = await fetch(`/job/${encoded}`);

		if (!response.ok) {
			throw new Error("Failed to load job details");
		}

		const job = await response.json();
		statusText.textContent = "";
		return job;
	} catch (error) {
		statusText.textContent = "Could not load details for this job.";
		return null;
	}
}

function closeJobsSublist(item) {
	const jobsContainer = item.querySelector(".jobs-container");
	if (jobsContainer) {
		jobsContainer.remove();
	}
	item.classList.remove("is-open");
	activeJobButton = null;
	renderJobDetails(null);
	if (activeGroupItem === item) {
		activeGroupItem = null;
	}
}

function renderJobsSublist(item, jobs) {
	const existingContainer = item.querySelector(".jobs-container");
	if (existingContainer) {
		existingContainer.remove();
 	}

	const jobsContainer = document.createElement("div");
	jobsContainer.className = "jobs-container";

	const jobsList = document.createElement("ul");
	jobsList.className = "jobs-list";

	if (!jobs || jobs.length === 0) {
		const emptyItem = document.createElement("li");
		emptyItem.textContent = "No jobs found for this group.";
		jobsList.appendChild(emptyItem);
	} else {
		jobs.forEach((job) => {
			const jobItem = document.createElement("li");

			const jobButton = document.createElement("button");
			jobButton.type = "button";
			jobButton.className = "job-trigger";
			jobButton.textContent = job.job_name;
			jobButton.addEventListener("click", async () => {
				if (activeJobButton) {
					activeJobButton.classList.remove("is-selected");
				}

				activeJobButton = jobButton;
				activeJobButton.classList.add("is-selected");

				const selectedJob = await loadJobDetails(job.job_name);
				if (selectedJob) {
					renderJobDetails(selectedJob);
				}
			});

			jobItem.appendChild(jobButton);
			jobsList.appendChild(jobItem);
		});
	}

	jobsContainer.appendChild(jobsList);
	item.appendChild(jobsContainer);
	item.classList.add("is-open");
	activeGroupItem = item;
}

async function handleGroupClick(group, item) {
	if (activeGroupItem && activeGroupItem !== item) {
		closeJobsSublist(activeGroupItem);
	}

	if (activeGroupItem === item) {
		closeJobsSublist(item);
		renderGroupDetails(null);
		statusText.textContent = "";
		return;
	}

	renderGroupDetails(group);
	const jobs = await loadJobsForGroup(group.job_group);
	if (jobs !== null) {
		renderJobsSublist(item, jobs);
	}
}

loadGroups();
