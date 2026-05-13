
# Workflows

The workflows/ directory contains orchestrated, multi-step procedures that coordinate multiple skills and rules to accomplish complex end-to-end tasks.

Unlike skills (which are single, focused capabilities), workflows are composed sequences that guide the AI through sophisticated processes involving multiple tools, validations, and decision points.

Each workflow:

  - Has a frontmatter with metadata (auto_execution_mode, description, dependencies)
  - Coordinates multiple skills in a specific sequence
  - Includes decision logic and branching paths
  - Provides comprehensive error handling and validation
  - Generates reports and documentation

How AI Uses Workflows

When you interact with Windsurf's AI:

  1. _Workflow Invocation_`: AI can invoke workflows based on user requests, triggers, or context.
  2. _Skill Orchestration_`: Workflows coordinate multiple skills in specific sequences.
  3. _Decision Logic_`: AI follows branching paths and conditional logic within workflows.
  4. _Error Handling_`: Workflows provide comprehensive error handling and recovery.
  5. _State Management_`: Some workflows maintain state (batch processing, resume capability).
  6. _Report Generation_`: Workflows generate detailed reports and documentation.

## Workflow Explanations

1. **analyze-and-update-tests.md**

  - `Purpose`: Analyzes current git changes and manages related test cases by updating existing ones or creating new ones
  - `AI Use`: Automatically identifies what code has changed, locates related tests, updates or creates tests to maintain coverage
  - `Key Features`: Git change analysis, test location, coverage impact analysis, AAA pattern enforcement, test generation
  - `Dependencies`: testing-setup skill
  - `Use Case`: "I just modified this service class - update the related tests"

2. **batch-check-and-fix-snyk-vulns.md**

  - `Purpose`: Batch processes multiple repositories to check and fix Snyk vulnerabilities with resume capability and dry-run mode
  - `AI Use`: Orchestrates large-scale vulnerability remediation across many repositories with state tracking
  - `Key Features`: Batch processing, resume capability, dry-run mode, severity filtering, auto-confirmation, state file persistence
  - `Dependencies`: snyk-export, check-and-fix-snyk-vulns
  - `Parameters`: --temp_dir, --batch_size, --dry_run, --severity_filter, --resume
  - `Use Case`: "Fix all Critical and High vulnerabilities across 25 repositories"

3. **check-and-fix-snyk-vulns.md**

  - `Purpose`: Performs Snyk security vulnerability checks and manages fixes with proper source branch selection and MR creation
  - `AI Use`: Complete vulnerability remediation workflow from scanning to MR creation
  - `Key Features`: MR checking for duplicates, Snyk authentication, vulnerability remediation (package + code-level), branch selection, MR creation
  - `Dependencies`: snyk-authenticator, gitlab-mr-checker, verify-and-commit, security-review, dell-source-branch-selection, dell-vulnerability-remediation, gitlab-mr-creation
  - `Parameters`: --org-id, --auth-method, --api-token, --fix-source-code
  - `Use Case`: "Scan this repository for vulnerabilities and create a fix with proper MR"

4. **configure-linting.md**

  - `Purpose`: Sets up comprehensive linting and code quality enforcement for .NET and React projects
  - `AI Use`: Configures linting infrastructure with proper tools, rules, and CI integration
  - `Key Features`: .NET linting (.editorconfig), React linting (ESLint, Stylelint, Prettier), package installation, CI integration
  - `Dependencies`: linting-configuration skill
  - `Use Case`: "Set up linting for my new project with enterprise standards"

5. **figma-to-dds-component.md**

  - `Purpose`: Creates or modifies components using Figma designs while ensuring full compliance with the Dell Design System (DDS)
  - `AI Use`: Translates Figma designs into DDS-compliant components across React, Angular, and Vanilla frameworks
  - `Key Features`: Figma MCP integration, DDS component mapping, approval gates (no custom CSS without approval), framework-agnostic
  - `Dependencies`: figma-remote-mcp-server
  - `Approval Rules`: Never write custom CSS or use non-DDS components without explicit user approval
  - `Use Case`: "Implement this Figma design using only DDS components"

6. **security-audit.md**

  - `Purpose`: Performs comprehensive security audit and configures security best practices with defense-in-depth architecture
  - `AI Use`: Complete security workflow including Vault integration, authentication, input validation, and vulnerability scanning
  - `Key Features`: HashiCorp Vault integration, JWT configuration, input validation, secrets management, Snyk scanning, threat modeling
  - `Dependencies`: security-review, snyk-authenticator, snyk-local
  - `Use Case`: "Audit this project's security posture and configure best practices"

7. **setup-testing.md**

  - `Purpose`: Configures project with comprehensive testing setup including unit, integration, and E2E tests with test pyramid architecture
  - `AI Use`: Establishes complete testing infrastructure with proper coverage gates and CI integration
  - `Key Features`: Test pyramid (80% unit, 15% integration, 5% E2E), .NET (xUnit, NSubstitute), React (Jest, RTL, MSW), coverage thresholds
  - `Dependencies`: testing-setup skill
  - `Use Case`: "Set up testing infrastructure for my new project with coverage gates"

8. **verify-and-commit.md**

  - `Purpose`: Performs comprehensive verification before committing code including tests, linting, security, and code quality review
  - `AI Use`: Complete pre-commit workflow with quality gates and MR creation
  - `Key Features`: Test execution, coverage verification, linting checks, security scanning, code quality review (9 focus areas), commit formatting, MR creation
  - `Dependencies`: setup-testing, configure-linting, security-audit, snyk-authenticator, snyk-local, dell-source-branch-selection, gitlab-mr-creation
  - `Code Review Focus Areas`: Logic errors, edge cases, null references, race conditions, security, resource management, API contracts, caching, code patterns
  - `Use Case`: "Verify my changes and create a commit with proper MR"

9. **fpp/remove-dds-overrides.md**

  - `Purpose`: Removes DDS CSS overrides when parent app updates DDS version to match proposals-mfe
  - `AI Use`: Guides testing and removal of temporary DDS version mismatch overrides
  - `Key Features`: Version mismatch detection, override testing, safe removal process
  - `Use Case`: "The parent app updated DDS - can we remove these overrides now?"
