from flask import Blueprint, render_template

solutions_bp = Blueprint(
    "solutions",
    __name__,
    url_prefix="/solutions"
)

@solutions_bp.route("/", endpoint="index")
def index():
    return render_template("solutions/index.html")


@solutions_bp.route("/infrastructure/", endpoint="infrastructure")
def infrastructure():
    return render_template("solutions/infrastructure.html")

@solutions_bp.route("/infrastructure/datacentre_infra/", endpoint="datacentre_infra")
def datacentre_infra():
    return render_template("solutions/infrastructures/datacentre.html")

@solutions_bp.route("/infrastructure/server_infra/", endpoint="server_infra")
def server_infra():
    return render_template("solutions/infrastructures/servers.html")

@solutions_bp.route("/infrastructure/monitoring_uptime/", endpoint="monitoring_uptime")
def monitoring_uptime():
    return render_template("solutions/infrastructures/monitoring_uptime.html")

@solutions_bp.route("/networking/", endpoint="networking")
def networking():
    return render_template("solutions/networking.html")

@solutions_bp.route("/networking/enterpise_networks/", endpoint="Enterprise_Networking")
def enterpise_networks():
    return render_template("solutions/networks/enterprise_lan_wan.html")

@solutions_bp.route("/networking/fibre_wireless/", endpoint="Fibre_Wireless")
def fibre_wireless():
    return render_template("solutions/networks/fibre_wireless.html")

@solutions_bp.route("/networking/5g/", endpoint="5G")
def fiveg():
    return render_template("solutions/networks/5g.html")

@solutions_bp.route("/cloud/", endpoint="cloud")
def cloud():
    return render_template("solutions/cloud.html")


@solutions_bp.route("/software/", endpoint="software")
def software():
    return render_template("solutions/software.html")

@solutions_bp.route("/software/deepfakedefence/", endpoint="deepfakedefence")
def deepfakedefence():
    return render_template("solutions/software/deepfakedefence.html")

@solutions_bp.route("/software/sentinelpi/", endpoint="sentinelpi")
def sentinelpi():
    return render_template("solutions/software/sentinelpi.html")

@solutions_bp.route("/software/kycidenetity/", endpoint="kycidenetity")
def kycidenetity():
    return render_template("solutions/software/kycidenetity.html")


@solutions_bp.route("/ai/", endpoint="ai")
def ai():
    return render_template("solutions/ai.html")


@solutions_bp.route("/security/", endpoint="security")
def security():
    return render_template("solutions/security.html")
