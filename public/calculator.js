function closestAgreementEndDate(calendarType, date) {
    const quarterEndDates = [
        "03-31",
        "06-30",
        "09-30",
        "12-31"
    ];

    const dateTypes = {
        "quarter": quarterEndDates
    };

    const currentYear = date.getFullYear();
    
    const formattedDates = [
        ...dateTypes[calendarType].map(d => new Date(`${currentYear}-${d}T00:00:00`)),
        ...dateTypes[calendarType].map(d => new Date(`${currentYear - 1}-${d}T00:00:00`))
    ];

    let nearestEndDate = null;

    for (let i = 0; i < formattedDates.length; i++) {
        const thisEnd = formattedDates[i];
        const lastEnd = formattedDates[(i - 1 + formattedDates.length) % formattedDates.length];

        if (lastEnd < date && date <= thisEnd) {
            nearestEndDate = thisEnd;
            break;
        } else if (lastEnd === date) {
            nearestEndDate = lastEnd;
            break;
        }
    }
    console.log(nearestEndDate)
    return nearestEndDate;
}

// Function to add days to a date
function addDays(endDate, days) {
    const result = new Date(endDate);
    result.setDate(result.getDate() + days);
    return result;
}

// Function to generate date ranges
function generateDateRanges(calendarType, startDate, endDate, requirementDays) {
    console.log(startDate)
    if (requirementDays <= 0) {
        return [[], []];
    }

    const requirements = [];
    let reqDate = closestAgreementEndDate(calendarType, startDate);

    while (reqDate < endDate) {
        const lo = reqDate;
        const hi = addDays(reqDate, requirementDays);
        requirements.push({ start: lo, end: hi });
        reqDate = closestAgreementEndDate(calendarType, addDays(hi, 1));
    }

    if (requirements.length > 0 && requirements[requirements.length - 1].end > endDate) {
        requirements.pop();
    }

    return [requirements[0] ? [requirements[0]] : [], requirements];
}

const myLink = document.getElementById('me-link')

myLink.addEventListener('mouseover', () => {
    myLink.textContent = "Created by: David S."
})

myLink.addEventListener('mouseout', () => {
    myLink.textContent = "Agreements Calculator"
})

// Function to handle the button click event
document.getElementById('calculateBtn').addEventListener('click', () => {
    const calendarType = document.getElementById('calendarType').value;
    const startDate = new Date(document.getElementById('startDate').value);
    const endDate = new Date(document.getElementById('endDate').value);
    const requirementDays = parseInt(document.getElementById('requirementDays').value);

    const [firstRange, allRanges] = generateDateRanges(calendarType, startDate, endDate, requirementDays);

    let csvContent = "";
    csvContent += "data:text/csv;charset=utf-8,"
    csvContent += "Quarter Start Date, Agreement End Date\n";

    let resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = "";
    resultsDiv.innerHTML = "<h3>Calculated Date Ranges:</h3>";

    if (allRanges.length > 0) {
        allRanges.forEach(range => {
            resultsDiv.innerHTML += `<p>${range.end.toLocaleDateString()}</p>`;
            csvContent += `${range.start.toLocaleDateString()}, ${range.end.toLocaleDateString()}\n`;
        });
    } else {
        resultsDiv.innerHTML += `<p>No valid ranges found.</p>`;
    }

    document.getElementById('downloadBtn').onclick = function() {
        const encodedUri = encodeURI(csvContent);
        const link = document.createElement("a");
        link.setAttribute("href", encodedUri);
        link.setAttribute("download", "date_ranges.csv");
        document.body.appendChild(link); // Required for Firefox
        link.click();
        document.body.removeChild(link); // Clean up the DOM
    };
});