const calcDisplay = document.getElementById('calcDisplay');
const buttonsContainer = document.querySelector('.buttons');
const clearButton = document.getElementById('clear');
const equalsButton = document.getElementById('equals');
const taxAmount = document.getElementById('taxAmount');
const gstRate = document.getElementById('gstRate');
const taxMode = document.getElementById('taxMode');
const calculateTaxButton = document.getElementById('calculateTax');
const taxResults = document.getElementById('taxResults');
const birthdayInput = document.getElementById('birthdayInput');
const calculateBirthdayButton = document.getElementById('calculateBirthday');
const birthdayResults = document.getElementById('birthdayResults');

let expression = '';

function updateDisplay() {
  calcDisplay.value = expression || '0';
}

buttonsContainer.addEventListener('click', (event) => {
  const button = event.target.closest('button');
  if (!button) {
    return;
  }

  if (button.id === 'clear') {
    expression = '';
    updateDisplay();
    return;
  }

  if (button.id === 'equals') {
    evaluateExpression();
    return;
  }

  const value = button.dataset.value;
  if (!value) {
    return;
  }

  if (expression === '' && ['+', '-', '*', '/'].includes(value)) {
    return;
  }

  const lastChar = expression.slice(-1);
  if (['+', '-', '*', '/'].includes(lastChar) && ['+', '-', '*', '/'].includes(value)) {
    expression = expression.slice(0, -1) + value;
  } else {
    expression += value;
  }

  updateDisplay();
});

function evaluateExpression() {
  if (!expression) {
    return;
  }

  try {
    const safeExpression = expression.replace(/×/g, '*').replace(/÷/g, '/');
    const result = Function('"use strict"; return (' + safeExpression + ')')();
    expression = String(result);
    updateDisplay();
  } catch (error) {
    calcDisplay.value = 'Error';
    expression = '';
  }
}

function formatCurrency(value) {
  return parseFloat(value).toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 });
}

calculateTaxButton.addEventListener('click', () => {
  const amount = parseFloat(taxAmount.value);
  const rate = parseFloat(gstRate.value);
  const mode = taxMode.value;

  if (Number.isNaN(amount) || Number.isNaN(rate)) {
    taxResults.textContent = 'Please enter a valid amount and GST rate.';
    return;
  }

  const decimalRate = rate / 100;
  let gstAmount, total;

  if (mode === 'exclusive') {
    gstAmount = amount * decimalRate;
    total = amount + gstAmount;
    taxResults.textContent = `Amount: ₹${formatCurrency(amount)}\nGST (${rate}%): ₹${formatCurrency(gstAmount)}\nTotal with GST: ₹${formatCurrency(total)}`;
  } else {
    total = amount;
    gstAmount = total - total / (1 + decimalRate);
    const netAmount = total - gstAmount;
    taxResults.textContent = `Total Amount: ₹${formatCurrency(total)}\nGST (${rate}%): ₹${formatCurrency(gstAmount)}\nNet Amount before GST: ₹${formatCurrency(netAmount)}`;
  }
});

calculateBirthdayButton.addEventListener('click', () => {
  const birthdayValue = birthdayInput.value;

  if (!birthdayValue) {
    birthdayResults.textContent = 'Please choose your birthday first.';
    return;
  }

  const birthDate = new Date(birthdayValue);
  const now = new Date();

  if (birthDate > now) {
    birthdayResults.textContent = 'Birthday cannot be in the future.';
    return;
  }

  const ageYears = now.getFullYear() - birthDate.getFullYear();
  const monthDiff = now.getMonth() - birthDate.getMonth();
  const dayDiff = now.getDate() - birthDate.getDate();

  let years = ageYears;
  let months = monthDiff;
  let days = dayDiff;

  if (days < 0) {
    const previousMonth = new Date(now.getFullYear(), now.getMonth(), 0);
    days += previousMonth.getDate();
    months -= 1;
  }

  if (months < 0) {
    months += 12;
    years -= 1;
  }

  const nextBirthday = new Date(now.getFullYear(), birthDate.getMonth(), birthDate.getDate());
  if (nextBirthday < now) {
    nextBirthday.setFullYear(now.getFullYear() + 1);
  }

  const diffMs = nextBirthday - now;
  const diffDays = Math.ceil(diffMs / (1000 * 60 * 60 * 24));

  birthdayResults.textContent = `Age: ${years} years, ${months} months, ${days} days\nDays until next birthday: ${diffDays}`;
});

updateDisplay();
