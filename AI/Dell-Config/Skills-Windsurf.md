
# Skills

The skills/ directory contains reusable AI capabilities that can be invoked on-demand to perform specific tasks. 

Unlike rules (which are always-on guardrails), skills are actionable workflows that the AI can invoke when needed to accomplish specific goals.

Each skill follows a standard structure:

  - `SKILL.md` - Main skill definition with frontmatter metadata
  - `scripts/` - Executable scripts for automation
  - `templates/` - Reusable templates and patterns
  - `checklists/` - Verification checklists
  - `references/` - Supporting documentation

The MANIFEST.json file registers all available skills and their enablement status.

## How AI Uses Skills

When you interact with Windsurf's AI:

  1. _Skill Invocation_: AI can invoke skills based on context, triggers, or explicit requests
  2. _Workflow Execution_: Skills provide step-by-step guidance that AI follows
  3. _Asset Utilization_: AI uses templates, checklists, and scripts within skill directories
  4. _Integration_: Skills can invoke other skills (dependencies) for complex workflows
  5. _Validation_: Each skill has validation criteria to ensure successful completion

## Skill Explanations

1. **business-kpis**

  - `Purpose`: Analyzes AI-assisted development initiatives to calculate ROI, time savings, and business impact
  - `AI Use`: Generates executive summaries, calculates engineer-days saved, produces KPI reports for leadership
  - `Key Features`: Time tracking analysis, ROI calculation, executive one-pager generation, portfolio aggregation
  - `Use Case`: "Show me the ROI of our AI-assisted development initiatives over the last quarter"

2. **cicd-onboarding**

  - `Purpose`: Onboards projects to unified CI/CD templates with platform-specific pipeline configuration
  - `AI Use`: Automates GitLab CI/CD pipeline setup for .NET, React, and hybrid projects
  - `Key Features`: Multi-platform support (PCF, KOB-ACE, KOB-Native, NPM, NuGet), security scanning integration, deployment automation
  - `Use Case`: "Set up CI/CD pipelines for my new .NET service using the unified templates"

3. **code-review**

  - `Purpose`: Performs comprehensive code review covering quality, security, performance, and best practices
  - `AI Use`: Conducts structured code reviews before merge, evaluating architecture, correctness, and testing
  - `Key Features`: Architecture review, code deep-dive, security verification, automated checks (lint, test, security scan)
  - `Use Case`: "Review this pull request for quality, security, and performance issues"

4. **create-skill**

  - `Purpose`: Scaffolds new Windsurf skills with consistent structure and validation guidance
  - `AI Use`: Creates new skill directories and SKILL.md files following framework conventions
  - `Key Features`: Standard skill structure, frontmatter generation, optional folder setup, validation checklist
  - `Use Case`: "Create a new skill for database migration automation"

5. **dds-docs / dds-react-docs**

  - `Purpose`: Reference documentation for the DDS React design system (@dds/react)
  - `AI Use`: Provides component API documentation when working with DDS React components
  - `Key Features`: Component documentation, token references, pattern examples, usage guidelines
  - `Use Case`: "How do I use the DDS Accordion component with custom styling?"

6. **dell-source-branch-selection**

  - `Purpose`: Determines source branch for merge requests using Dell-specific fiscal year format
  - `AI Use`: Selects appropriate source branches (main/master or release branches) for GitLab MRs
  - `Key Features`: Dell fiscal year branch parsing (release-fy<-<*), oldest branch selection, cross-platform support
  - `Use Case`: "Which source branch should I use for this merge request?"

7. **dell-vulnerability-remediation**

  - `Purpose`: Applies Dell-specific vulnerability remediation patterns for security fixes
  - `AI Use`: Automates vulnerability remediation with Dell-specific patterns (Commerce libraries, AutoMapper replacement)
  - `Key Features`: Commerce library updates, AutoMapper replacement, common vulnerable package fixes, transitive dependency handling
  - `Use Case`: "Fix the AutoMapper vulnerabilities found in the Snyk scan"

8. **gitlab-cli-setup**

  - `Purpose`: Installs GitLab CLI (glab) via Scoop and authenticates with gitlab.dell.com
  - `AI Use`: Sets up GitLab CLI foundation for all GitLab operations (MR creation, checking)
  - `Key Features`: Scoop installation, interactive authentication, cross-platform support (PowerShell/Bash)
  - `Use Case`: "Set up GitLab CLI so I can create merge requests"

9. **gitlab-mr-checker**

  - `Purpose`: Checks for existing open merge requests related to vulnerability fixes to prevent duplicates
  - `AI Use`: Queries GitLab for existing MRs, analyzes vulnerability coverage, prevents duplicate remediation
  - `Key Features`: Open MR query, vulnerability analysis, decision logic, reporting
  - `Use Case`: "Check if there's already an MR open for this AutoMapper vulnerability"

10. **gitlab-mr-creation**

  - `Purpose`: Creates GitLab merge requests using glab CLI with security-focused template
  - `AI Use`: Automates MR creation with security verification, Jira ID extraction, label management
  - `Key Features`: Auto-generated descriptions, Jira ID extraction, label management, squash/delete branch configuration
  - `Use Case`: "Create a merge request for these vulnerability fixes with proper security documentation"

11. **snyk-authenticator**

  - `Purpose`: Handles Snyk authentication with support for API tokens, CLI browser login, and environment variables
  - `AI Use`: Manages Snyk authentication for vulnerability scanning operations
  - `Key Features`: Multiple auth methods (token, CLI, auto), organization configuration, authentication verification
  - `Use Case`: "Authenticate with Snyk so I can run vulnerability scans"

12. **snyk-export**

  - `Purpose`: Downloads Snyk vulnerability reports from Snyk cloud using Export API, converts CSV to JSON
  - `AI Use`: Exports vulnerability data for compliance reporting, converts formats, filters by severity
  - `Key Features`: Cloud-based reports, CSV export, JSON conversion, severity filtering, repository extraction
  - `Use Case`: "Download all Critical and High vulnerabilities from Snyk cloud for our compliance report"

13. **snyk-local**

  - `Purpose`: Install, authenticate, and run Snyk security scanning locally for vulnerability detection
  - `AI Use`: Guides local Snyk CLI setup and execution for SCA and SAST scanning
  - `Key Features`: SCA scanning (dependencies), SAST scanning (code), severity thresholds, IDE integration
  - `Use Case`: "Run a local Snyk scan to check for vulnerabilities in my project"

14. **spec-driven-development**

  - `Purpose`: Translates Jira tickets into fully specified, AI-implementable work items
  - `AI Use`: Creates structured specifications that Cascade can implement deterministically
  - `Key Features`: SDD methodology, acceptance criteria generation, technical design, change manifest
  - `Use Case`: "Create a detailed specification for this Jira ticket so AI can implement it"

15. **testing-setup**

  - `Purpose`: Sets up comprehensive testing framework with templates, configurations, and automated test generation
  - `AI Use`: Establishes testing infrastructure, generates tests, enforces coverage gates
  - `Key Features`: .NET (xUnit, NSubstitute), React (Jest, RTL), coverage configuration, CI integration
  - `Use Case`: "Set up testing infrastructure for my new React project with coverage gates"

16. **verify-and-commit**

  - `Purpose`: Comprehensive pre-commit verification and git commit workflow with automated quality gates
  - `AI Use`: Runs complete quality/security checks before committing, creates standards-compliant commits
  - `Key Features`: Code quality checks, build verification, test execution, security scans, commit message formatting
  - `Use Case`: "Verify my changes and create a commit with proper formatting"

17. **linting-configuration**

  - `Purpose`: Configures comprehensive linting and code quality enforcement with automated setup
  - `AI Use`: Sets up linting baselines for .NET and React projects with CI compatibility
  - `Key Features`: .NET (.editorconfig), React (ESLint, Prettier, Stylelint), automation, CI integration
  - `Use Case`: "Set up linting for my project with consistent rules across IDE and CI"

18. **security-review**

  - `Purpose`: Performs comprehensive security audit with checklists, templates, and automated vulnerability scanning
  - `AI Use`: Conducts security reviews, validates auth/input/secrets, runs vulnerability scans
  - `Key Features`: Authentication review, input validation, secrets management, SAST/dependency scanning, compliance checks
  - `Use Case`: "Review this authentication implementation for security issues"



