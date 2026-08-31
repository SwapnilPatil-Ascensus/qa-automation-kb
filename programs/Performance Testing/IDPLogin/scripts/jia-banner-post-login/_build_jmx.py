"""Build idp-login-resources.jmx with 6 post-login dashboard page GETs."""
from pathlib import Path

SOURCE = Path(
    r"C:\Workspace\GitLab\Automation\performance-test-automation\performance\universal-platform\idp\jmeter\idp-login-resources.jmx"
)
TARGET = Path(__file__).resolve().parent / "idp-login-resources.jmx"

PAGES = [
    ("8-A-1. Auth Custom Banner (CS)", "customBannerMessage.cs", "${plan-tpl}/auth/customBannerMessage.cs"),
    ("8-A-2. Auth Side Banner (CS)", "sideBannerMessage.cs", "${plan-tpl}/auth/sideBannerMessage.cs"),
    ("8-A-3. AL Custom Banner (CS)", "customBannerMessage.cs", "${plan-tpl}/al/customBannerMessage.cs"),
    ("8-A-4. AO Custom Banner (CS)", "customBannerMessage.cs", "${plan-tpl}/ao/customBannerMessage.cs"),
    ("8-A-5. AO Overview (CS)", "overview.cs", "${plan-tpl}/ao/overview.cs"),
    ("8-A-6. AL List (CS)", "list.cs", "${plan-tpl}/al/list.cs"),
]

HEADER_BLOCK = """            <HeaderManager guiclass="HeaderPanel" testclass="HeaderManager" testname="HTTP Header Manager" enabled="true">
              <collectionProp name="HeaderManager.headers">
                <elementProp name="Accept-Language" elementType="Header">
                  <stringProp name="Header.name">Accept-Language</stringProp>
                  <stringProp name="Header.value">en-US,en;q=0.5</stringProp>
                </elementProp>
                <elementProp name="Upgrade-Insecure-Requests" elementType="Header">
                  <stringProp name="Header.name">Upgrade-Insecure-Requests</stringProp>
                  <stringProp name="Header.value">1</stringProp>
                </elementProp>
                <elementProp name="Accept-Encoding" elementType="Header">
                  <stringProp name="Header.name">Accept-Encoding</stringProp>
                  <stringProp name="Header.value">gzip, deflate, br</stringProp>
                </elementProp>
                <elementProp name="User-Agent" elementType="Header">
                  <stringProp name="Header.name">User-Agent</stringProp>
                  <stringProp name="Header.value">Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0</stringProp>
                </elementProp>
                <elementProp name="Accept" elementType="Header">
                  <stringProp name="Header.name">Accept</stringProp>
                  <stringProp name="Header.value">text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8</stringProp>
                </elementProp>
                <elementProp name="" elementType="Header">
                  <stringProp name="Header.name">x-sardine-session-key</stringProp>
                  <stringProp name="Header.value">${sardinekey}</stringProp>
                </elementProp>
              </collectionProp>
            </HeaderManager>
            <hashTree/>
            <ResponseAssertion guiclass="AssertionGui" testclass="ResponseAssertion" testname="Assert Status 200" enabled="true">
              <collectionProp name="Asserion.test_strings">
                <stringProp name="49586">200</stringProp>
              </collectionProp>
              <stringProp name="Assertion.custom_message"></stringProp>
              <stringProp name="Assertion.test_field">Assertion.response_code</stringProp>
              <boolProp name="Assertion.assume_success">false</boolProp>
              <intProp name="Assertion.test_type">8</intProp>
            </ResponseAssertion>
            <hashTree/>
            <ResponseAssertion guiclass="AssertionGui" testclass="ResponseAssertion" testname="Assert Site Not Unavailable" enabled="true">
              <collectionProp name="Asserion.test_strings">
                <stringProp name="1537278">unavailable</stringProp>
              </collectionProp>
              <stringProp name="Assertion.custom_message">Site unavailable on ${__samplerName}</stringProp>
              <stringProp name="Assertion.test_field">Assertion.response_data</stringProp>
              <boolProp name="Assertion.assume_success">false</boolProp>
              <intProp name="Assertion.test_type">6</intProp>
            </ResponseAssertion>
            <hashTree/>"""


def sampler_block(label: str, comment: str, path: str) -> str:
    return f"""          <HTTPSamplerProxy guiclass="HttpTestSampleGui" testclass="HTTPSamplerProxy" testname="{label}" enabled="true">
            <stringProp name="TestPlan.comments">{comment}</stringProp>
            <intProp name="HTTPSampler.concurrentPool">6</intProp>
            <stringProp name="HTTPSampler.domain">${{domain-host}}</stringProp>
            <stringProp name="HTTPSampler.port">443</stringProp>
            <stringProp name="HTTPSampler.protocol">https</stringProp>
            <stringProp name="HTTPSampler.path">{path}</stringProp>
            <boolProp name="HTTPSampler.follow_redirects">true</boolProp>
            <stringProp name="HTTPSampler.method">GET</stringProp>
            <boolProp name="HTTPSampler.use_keepalive">true</boolProp>
            <boolProp name="HTTPSampler.postBodyRaw">false</boolProp>
            <elementProp name="HTTPsampler.Arguments" elementType="Arguments" guiclass="HTTPArgumentsPanel" testclass="Arguments" testname="User Defined Variables">
              <collectionProp name="Arguments.arguments"/>
            </elementProp>
          </HTTPSamplerProxy>
          <hashTree>
{HEADER_BLOCK}
          </hashTree>"""


def build_insert() -> str:
    samplers = "\n".join(sampler_block(label, comment, path) for label, comment, path in PAGES)
    return f"""        <GenericController guiclass="LogicControllerGui" testclass="GenericController" testname="8-A. Post-Login Dashboard Pages (CS)" enabled="true"/>
        <hashTree>
{samplers}
        </hashTree>
"""


def main() -> None:
    content = SOURCE.read_text(encoding="utf-8")
    marker = '        <GenericController guiclass="LogicControllerGui" testclass="GenericController" testname="9. Logout (CS)"'
    if marker not in content:
        raise SystemExit("Logout marker not found in source JMX")
    if "8-A. Post-Login Dashboard Pages (CS)" in content:
        raise SystemExit("Post-login block already present in source JMX")

    content = content.replace(marker, build_insert() + marker, 1)
    TARGET.write_text(content, encoding="utf-8", newline="\n")
    print(f"Wrote {TARGET}")


if __name__ == "__main__":
    main()
