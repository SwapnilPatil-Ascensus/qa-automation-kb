import fs from 'fs';
import puppeteer from 'puppeteer'; // v20.7.4 or later

(async () => {

    const browser = await puppeteer.launch({headless: false});
    const page = await browser.newPage();
    const timeout = 5000;
    page.setDefaultTimeout(timeout);

    const lhApi = await import('lighthouse'); // v10.0.0 or later
    const flags = {
        screenEmulation: {
            disabled: true
        }
    }
    const config = lhApi.desktopConfig;
    const lhFlow = await lhApi.startFlow(page, {name: 'Universal Enrollment - Check, Custom', config, flags});
    {
        const targetPage = page;
        await targetPage.setViewport({
            width: 971,
            height: 743
        })
    }
    await lhFlow.startNavigation({ name: "Navigate to enrollment" });
    {
        const targetPage = page;
        const promises = [];
        const startWaitingForEvents = () => {
            promises.push(targetPage.waitForNavigation());
        }
        startWaitingForEvents();
        await targetPage.goto('https://agsup-ui-enrollment-qc4.gs.ascensus.com/enrollments/newyork');
        await Promise.all(promises);
    }
    await lhFlow.endNavigation();

    await lhFlow.startTimespan({ name: "Filling prospect details" });
    {
        const targetPage = page;
        await targetPage.locator('#firstName')
            .setTimeout(timeout)
            .fill('Jill');
    }
    {
        const targetPage = page;
        await targetPage.locator('#lastName')
            .setTimeout(timeout)
            .fill('Smith');
    }
    {
        const targetPage = page;
        await targetPage.locator('#email input')
            .setTimeout(timeout)
            .fill('tester@123.com');
    }
    {
        const targetPage = page;
        await targetPage.locator('#confirmEmail input')
            .setTimeout(timeout)
            .fill('tester@123.com');
    }
    {
        const targetPage = page;
        await targetPage.locator('#username')
            .setTimeout(timeout)
            .fill('tester' + (Math.floor(Math.random() * 999999) + 100000));
    }
    {
        const targetPage = page;
        await targetPage.locator('#password input')
            .setTimeout(timeout)
            .fill('Test@123');
    }
    {
        const targetPage = page;
        await targetPage.locator('#confirmPassword input')
            .setTimeout(timeout)
            .fill('Test@123');
    }
    await lhFlow.endTimespan();
    await lhFlow.snapshot({ name: "Filled out prospect" });

    await lhFlow.startTimespan({ name: "Submit prospect" });
    {
        const targetPage = page;
        await targetPage.locator('#createLogin')
            .setTimeout(timeout)
            .click({
              offset: {
                x: 1,
                y: 1,
              },
            });
    }
    await lhFlow.endTimespan();
    
    await lhFlow.startTimespan({ name: "Filling owner details" });
    {
        const targetPage = page;
        await targetPage.locator('#acct-details-phone-number >>>> input')
            .setTimeout(timeout)
            .click();
        await targetPage.locator('#acct-details-phone-number >>>> input')
            .setTimeout(timeout)
            .fill('2223331111');
    }
    {
        const targetPage = page;
        await targetPage.locator('#acct-details-phone-type')
            .setTimeout(timeout)
            .click({
              offset: {
                x: 1,
                y: 1,
              },
            });
    }
    {
        const targetPage = page;
        await targetPage.locator('kendo-popup li:first-child')
            .setTimeout(timeout)
            .click({
              offset: {
                x: 1,
                y: 1,
              },
            });
    }
	const ownerssn = (Math.floor(Math.random() * 899999999) + 100000000);
    {
        const targetPage = page;
        await targetPage.locator('#acct-details-ssn input')
            .setTimeout(timeout)
            .click();
        await targetPage.locator('#acct-details-ssn input')
            .setTimeout(timeout)
            .fill(ownerssn.toString());
    }
    {
        const targetPage = page;
        await targetPage.locator('#acct-details-confirm-ssn input')
            .setTimeout(timeout)
            .click();
        await targetPage.locator('#acct-details-confirm-ssn input')
            .setTimeout(timeout)
            .fill(ownerssn.toString());
    }
    {
        const targetPage = page;
        await targetPage.locator('#acct-details-dob >>>> input')
            .setTimeout(timeout)
            .click();
        await targetPage.locator('#acct-details-dob >>>> input')
            .setTimeout(timeout)
            .fill('11111990');
    }
    {
        const targetPage = page;
        await targetPage.locator('#acct-details-citizen')
            .setTimeout(timeout)
            .click({
              offset: {
                x: 1,
                y: 1,
              },
            });
    }
    {
        const targetPage = page;
        await targetPage.locator('kendo-popup li:first-child')
            .setTimeout(timeout)
            .click({
              offset: {
                x: 1,
                y: 1,
              },
            });
    }
    await lhFlow.endTimespan();
    await lhFlow.snapshot({ name: "Filled out owner details" });

    await lhFlow.startTimespan({ name: "Submit owner details" });
    {
        const targetPage = page;
        await targetPage.locator('#bottomNavPrimaryBtn')
            .setTimeout(timeout)
            .click({
              offset: {
                x: 1,
                y: 1,
              },
            });
    }
    await lhFlow.endTimespan();

    await lhFlow.startTimespan({ name: "Filling owner address" });
    {
        const targetPage = page;
        await targetPage.locator('#address1')
            .setTimeout(timeout)
            .fill('123 Main Street');
    }
    {
        const targetPage = page;
        await targetPage.locator('#city')
            .setTimeout(timeout)
            .fill('Newton');
    }
    {
        const targetPage = page;
        await targetPage.locator('#state')
            .setTimeout(timeout)
            .click({
              offset: {
                x: 1,
                y: 1,
              },
            });
    }
    {
        const targetPage = page;
        await targetPage.locator('kendo-popup li:nth-of-type(26)')
            .setTimeout(timeout)
            .click({
              offset: {
                x: 1,
                y: 1,
              },
            });
    }
    {
        const targetPage = page;
        await targetPage.locator('#zipcode')
            .setTimeout(timeout)
            .fill('02459');
    }
    {
        const targetPage = page;
        await targetPage.locator('#workInStateYes')
            .setTimeout(timeout)
            .click({
              offset: {
                x: 1,
                y: 1,
              },
            });
    }
    await lhFlow.endTimespan();
    await lhFlow.snapshot({ name: "Filled out owner address" });

    await lhFlow.startTimespan({ name: "Submit owner address" });
    {
        const targetPage = page;
        await targetPage.locator('#bottomNavPrimaryBtn')
            .setTimeout(timeout)
            .click({
              offset: {
                x: 1,
                y: 1,
              },
            });
    }
    await lhFlow.endTimespan();

    await lhFlow.startTimespan({ name: "Filling saving for" });
    {
        const targetPage = page;
        await targetPage.locator('#relationshipChild')
            .setTimeout(timeout)
            .click({
              offset: {
                x: 1,
                y: 1,
              },
            });
    }
    await lhFlow.endTimespan();
    await lhFlow.snapshot({ name: "Filled out saving for" });

	await lhFlow.startTimespan({ name: "Submit saving for" });
    {
        const targetPage = page;
        await targetPage.locator('#bottomNavPrimaryBtn')
            .setTimeout(timeout)
            .click({
              offset: {
                x: 1,
                y: 1,
              },
            });
    }
    await lhFlow.endTimespan();

    await lhFlow.startTimespan({ name: "Filling beneficiary details" });
    {
        const targetPage = page;
        await targetPage.locator('#bene-first-name')
            .setTimeout(timeout)
            .fill('Jill');
    }
    {
        const targetPage = page;
        await targetPage.locator('#bene-last-name')
            .setTimeout(timeout)
            .fill('Smith');
    }
	const benessn = (Math.floor(Math.random() * 899999999) + 100000000);
    {
        const targetPage = page;
        await targetPage.locator('#bene-ssn input')
            .setTimeout(timeout)
            .click();
        await targetPage.locator('#bene-ssn input')
            .setTimeout(timeout)
            .fill(benessn.toString());
    }
    {
        const targetPage = page;
        await targetPage.locator('#bene-confirm-ssn input')
            .setTimeout(timeout)
            .click();
        await targetPage.locator('#bene-confirm-ssn input')
            .setTimeout(timeout)
            .fill(benessn.toString());
    }
    {
        const targetPage = page;
        await targetPage.locator('#bene-dob input')
            .setTimeout(timeout)
            .click();
        await targetPage.locator('#bene-dob input')
            .setTimeout(timeout)
            .fill('11112000');
    }
    {
        const targetPage = page;
        await targetPage.locator('#acct-details-citizen')
            .setTimeout(timeout)
            .click({
              offset: {
                x: 1,
                y: 1,
              },
            });
    }
    {
        const targetPage = page;
        await targetPage.locator('kendo-popup li:first-child')
            .setTimeout(timeout)
            .click({
              offset: {
                x: 1,
                y: 1,
              },
            });
    }
    await lhFlow.endTimespan();
    await lhFlow.snapshot({ name: "Filled out beneficiary details" });

	await lhFlow.startTimespan({ name: "Submit beneficiary details" });
    {
        const targetPage = page;
        await targetPage.locator('#bottomNavPrimaryBtn')
            .setTimeout(timeout)
            .click({
              offset: {
                x: 1,
                y: 1,
              },
            });
    }
    await lhFlow.endTimespan();

    await lhFlow.startTimespan({ name: "Filling funding details" });
    {
        const targetPage = page;
        await targetPage.locator('#contribution-type')
            .setTimeout(timeout)
            .click({
              offset: {
                x: 1,
                y: 1,
              },
            });
    }
    {
        const targetPage = page;
        await targetPage.locator('kendo-popup li:nth-of-type(1)')
            .setTimeout(timeout)
            .click({
              offset: {
                x: 1,
                y: 1,
              },
            });
    }
    await lhFlow.endTimespan();
    await lhFlow.snapshot({ name: "Filled out funding details" });

	await lhFlow.startTimespan({ name: "Submit funding details" });
    {
        const targetPage = page;
        await targetPage.locator('#bottomNavPrimaryBtn')
            .setTimeout(timeout)
            .click({
              offset: {
                x: 1,
                y: 1,
              },
            });
    }
    await lhFlow.endTimespan();
    await lhFlow.snapshot({ name: "Review recurring details" });

    await lhFlow.startTimespan({ name: "Skip recurring details" });
    {
        const targetPage = page;
        await targetPage.locator('#skip-recurring')
            .setTimeout(timeout)
            .click({
              offset: {
                x: 1,
                y: 1,
              },
            });
    }
    await lhFlow.endTimespan();

    await lhFlow.startTimespan({ name: "Filling how to invest" });
    {
        const targetPage = page;
        await targetPage.locator('#build-your-own')
            .setTimeout(timeout)
            .click({
              offset: {
                x: 1,
                y: 1,
              },
            });
    }
    await lhFlow.endTimespan();
    await lhFlow.snapshot({ name: "Filled out how to invest" });

	await lhFlow.startTimespan({ name: "Submit how to invest" });
    {
        const targetPage = page;
        await targetPage.locator('#bottomNavPrimaryBtn')
            .setTimeout(timeout)
            .click({
              offset: {
                x: 1,
                y: 1,
              },
            });
    }
    await lhFlow.endTimespan();

    await lhFlow.startTimespan({ name: "Filling investment fund details" });
    {
        const targetPage = page;
        await targetPage.locator("input[type='checkbox']")
            .setTimeout(timeout)
            .click({
              offset: {
                x: 1,
                y: 1,
              },
            });
    }
    await lhFlow.endTimespan();
    await lhFlow.snapshot({ name: "Filled out investment fund details" });

	await lhFlow.startTimespan({ name: "Submit investment fund details" });
    {
        const targetPage = page;
        await targetPage.locator('#bottomNavPrimaryBtn')
            .setTimeout(timeout)
            .click({
              offset: {
                x: 1,
                y: 1,
              },
            });
    }
    await lhFlow.endTimespan();

    await lhFlow.startTimespan({ name: "Filling investment allocations" });
    {
        const targetPage = page;
        await targetPage.locator('kendo-numerictextbox input')
            .setTimeout(timeout)
            .fill('100');
    }
    await lhFlow.endTimespan();
    await lhFlow.snapshot({ name: "Filled out investment allocations" });

	await lhFlow.startTimespan({ name: "Submit investment allocations" });
    {
        const targetPage = page;
        await targetPage.locator('#bottomNavPrimaryBtn')
            .setTimeout(timeout)
            .click({
              offset: {
                x: 1,
                y: 1,
              },
            });
    }
    await lhFlow.endTimespan();
    await lhFlow.snapshot({ name: "Review for another beneficiary popup" });

	await lhFlow.startTimespan({ name: "Submit beneficiary popup" });
    {
        const targetPage = page;
        await targetPage.locator('#continue-btn-add-bene button:nth-of-type(2)')
            .setTimeout(timeout)
            .click({
              offset: {
                x: 1,
                y: 1,
              },
            });
    }
    await lhFlow.endTimespan();
    await lhFlow.snapshot({ name: "Review for upromise popup" });

    await lhFlow.startTimespan({ name: "Submit upromise popup" });
    {
        const targetPage = page;
        await targetPage.locator('#not-right-now')
            .setTimeout(timeout)
            .click({
              offset: {
                x: 1,
                y: 1,
              },
            });
    }
    await lhFlow.endTimespan();

    await lhFlow.startTimespan({ name: "Filling how review" });
    {
        const targetPage = page;
        await targetPage.locator('#delivery-checkbox')
            .setTimeout(timeout)
            .click({
              offset: {
                x: 1,
                y: 1,
              },
            });
    }
    {
        const targetPage = page;
        await targetPage.locator('#terms-checkbox')
            .setTimeout(timeout)
            .click({
              offset: {
                x: 1,
                y: 1,
              },
            });
    }
    await lhFlow.endTimespan();
    await lhFlow.snapshot({ name: "Filled out review" });

	await lhFlow.startTimespan({ name: "Submit review" });
    {
        const targetPage = page;
        await targetPage.locator('#bottomNavPrimaryBtn')
            .setTimeout(timeout)
            .click({
              offset: {
                x: 1,
                y: 1,
              },
            });
    }
    await lhFlow.endTimespan();
	await page.waitForSelector('ue-print-form');
    await lhFlow.snapshot({ name: "Review for print form" });

    {
        const targetPage = page;
        await targetPage.locator("span[class*='close']")
            .setTimeout(timeout)
            .click({
              offset: {
                x: 1,
                y: 1,
              },
            });
    }
    await lhFlow.snapshot({ name: "Review for account created" });

    const lhFlowReport = await lhFlow.generateReport();
    fs.writeFileSync('flow.report.html', lhFlowReport)

    await browser.close();

})().catch(err => {
    console.error(err);
    process.exit(1);
});
