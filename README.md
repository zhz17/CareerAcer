# Career Acer

![Anthropic](https://techcrunch.com/wp-content/uploads/2023/05/anthropic-header.jpg)

### Please note: An anthropic api key is required to run this project.

## 🚀 Project Overview

**Career Acer** is an intelligent Agent build with Model Context Protocol (MCP) which designed to analyze career pages and job postings from any company website. By processing job titles and descriptions, the agent predicts the typical interview process and generates a list of potential interview questions you might encounter for that role.

## ✨ Features

- **Job Advertisement Analysis:** Input a URL to a career or job posting page; the agent extracts and understands the job title and description.
- **Interview Process Prediction:** Based on the company and role, the agent predicts the likely interview stages (e.g., phone screen, technical, behavioural).
- **Potential Questions Generation:** Produces a list of tailored interview questions you may be asked, including technical, behavioural, and company-specific topics.
- **Matching Analysis:** Based on the job information and cv, analysis of the match between the job requirements and the candidate's qualifications.
- **User-Friendly:** Simple interface for inputting job URLs and receiving structured output.
- **Customizable:** Works for a wide range of companies and job types.

## 🛠️ How It Works

1. **Input:** Provide a link to a job posting or career page, and optionally a CV.
2. **Extraction:** The agent scrapes and parses the job title and description.
3. **Analysis:** Using AI, it infers the company's typical interview process and likely questions.
4. **Output:** You receive a structured summary of the interview process and a list of potential questions.

## 📦 Example Usage

```python
# replace 'your_anthropic_api_key' with your actual API key

python ./carerracer/ca_chatbot.py
```

## 💡 Use Cases

- **Job Seekers:** Prepare for interviews with company-specific insights.
- **Career Coaches:** Help clients anticipate and practice for real interview scenarios.
- **Recruiters:** Benchmark your own interview process against industry standards.

## 📈 Roadmap

- [x] Job Advertisement Analysis functinoality
- [x] Potential Questions Generation functionality
- [x] Matching Analysis functionality
- [ ] Intergration with free lmm api providers (e.g., Cerebras)
- [ ] User Interface for input and output
- [ ] (Maybe) Integration with popular job boards (e.g., Indeed, Glassdoor)

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## 📄 License

MIT License
