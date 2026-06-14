# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--14_09:54:30_UTC-green)

![Flight Map](images/flight_map.png)

## About

Historical archive of saved air traffic routes collected from the [OpenSky Network](https://opensky-network.org/) API. This repository keeps appending completed flights to `data/flights/` and rebuilds the visuals from the full archive.

**Data Source:** Saved route files in `data/flights/` (originally fetched from OpenSky `/flights/all`)

**Update Frequency:** Every 5 minutes via GitHub Actions

**How it works:**
- Fetches recently completed routes from OpenSky
- Saves each route as a JSON file in `data/flights/`
- Rebuilds aggregate statistics from all saved historical routes
- Generates a historical route map and archive summary
- Generates daily reports, weekly leaderboards, and timelapse GIFs

## Route Timelapse

![Timelapse](images/timelapse.gif)

## Archive Snapshot

**Latest saved flight:** 2026-06-14 09:54:30 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-14 09:54:30 UTC

- **109,816** saved flights
- **38,342** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **109,816** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,342,582.5 tonnes** estimated CO2 emissions
- **77,830,868 km** total distance flown
- **863 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4524 |
| 2 | SkyWest Airlines | 4110 |
| 3 | IndiGo | 2164 |
| 4 | EJA | 2107 |
| 5 | American Airlines | 1732 |
| 6 | Southwest Airlines | 1647 |
| 7 | ENY | 1362 |
| 8 | Delta Air Lines | 1296 |
| 9 | Lufthansa | 1246 |
| 10 | Vueling | 1007 |
| 11 | LATAM Airlines | 969 |
| 12 | WIF | 964 |
| 13 | AXM | 931 |
| 14 | AZU | 906 |
| 15 | LXJ | 828 |
| 16 | Swiss International | 794 |
| 17 | All Nippon Airways | 767 |
| 18 | Alaska Airlines | 749 |
| 19 | QLK | 726 |
| 20 | easyJet | 708 |
| 21 | EJU | 699 |
| 22 | Cathay Pacific | 655 |
| 23 | AEE | 623 |
| 24 | VIV | 619 |
| 25 | Air France | 618 |
| 26 | United Airlines | 607 |
| 27 | MXY | 586 |
| 28 | CXK | 576 |
| 29 | AXB | 543 |
| 30 | Japan Airlines | 541 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 92284 |
| 2 | 🇪🇸 ES | 7541 |
| 3 | 🇮🇳 IN | 6829 |
| 4 | 🇦🇺 AU | 6563 |
| 5 | 🇧🇷 BR | 6053 |
| 6 | 🇩🇪 DE | 5888 |
| 7 | 🇮🇹 IT | 5877 |
| 8 | 🇨🇦 CA | 5750 |
| 9 | 🇯🇵 JP | 5006 |
| 10 | 🇬🇧 GB | 4696 |
| 11 | 🇫🇷 FR | 4390 |
| 12 | 🇨🇴 CO | 3759 |
| 13 | 🇲🇽 MX | 3267 |
| 14 | 🇬🇷 GR | 3128 |
| 15 | 🇳🇴 NO | 3030 |
| 16 | 🇨🇭 CH | 2817 |
| 17 | 🇲🇾 MY | 2400 |
| 18 | 🇹🇷 TR | 2157 |
| 19 | 🇿🇦 ZA | 1879 |
| 20 | 🇰🇷 KR | 1842 |
| 21 | 🇹🇭 TH | 1820 |
| 22 | 🇳🇿 NZ | 1807 |
| 23 | 🇵🇱 PL | 1804 |
| 24 | 🇵🇭 PH | 1609 |
| 25 | 🇬🇹 GT | 1570 |
| 26 | 🇲🇦 MA | 1208 |
| 27 | 🇲🇴 MO | 1149 |
| 28 | 🇳🇱 NL | 1075 |
| 29 | 🇲🇪 ME | 1069 |
| 30 | 🇭🇷 HR | 956 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2354 |
| 2 | Denver International Airport |  | US | 1861 |
| 3 | Tokyo International Airport |  | JP | 1659 |
| 4 | Indira Gandhi International Airport |  | IN | 1485 |
| 5 | Guaymaral Airport |  | CO | 1393 |
| 6 | Harry Reid International Airport |  | US | 1388 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1372 |
| 8 | Zurich Airport |  | CH | 1241 |
| 9 | Frankfurt am Main International Airport |  | DE | 1225 |
| 10 | La Aurora Airport |  | GT | 1208 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1173 |
| 12 | Macau International Airport |  | MO | 1149 |
| 13 | El Dorado International Airport |  | CO | 1134 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1098 |
| 15 | Chicago O'Hare International Airport |  | US | 1088 |
| 16 | Madrid Barajas International Airport |  | ES | 957 |
| 17 | Capua Airport |  | IT | 942 |
| 18 | Kuala Lumpur International Airport |  | MY | 939 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 930 |
| 20 | Salt Lake City International Airport |  | US | 927 |
| 21 | Charlotte/Douglas International Airport |  | US | 845 |
| 22 | Congonhas Airport |  | BR | 838 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 833 |
| 24 | Charles de Gaulle International Airport |  | FR | 826 |
| 25 | Bengaluru International Airport |  | IN | 826 |
| 26 | Malpensa International Airport |  | IT | 801 |
| 27 | Ninoy Aquino International Airport |  | PH | 741 |
| 28 | Daniel K Inouye International Airport |  | US | 734 |
| 29 | General Edward Lawrence Logan International Airport |  | US | 730 |
| 30 | Tenerife Norte Airport |  | ES | 728 |
| 31 | Barcelona International Airport |  | ES | 721 |
| 32 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 714 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 702 |
| 34 | Amsterdam Airport Schiphol |  | NL | 665 |
| 35 | Don Mueang International Airport |  | TH | 664 |
| 36 | Vitoria/Foronda Airport |  | ES | 649 |
| 37 | Calgary International Airport |  | CA | 647 |
| 38 | Seattle-Tacoma International Airport |  | US | 631 |
| 39 | Norman Y Mineta San Jose International Airport |  | US | 629 |
| 40 | Viracopos International Airport |  | BR | 620 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 577 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 402 | 21m | 244 km | 1,692.7 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 295 | 24m | 225 km | 1,144.5 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 284 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 283 | 1h 7m | 706 km | 3,445.5 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 274 | 14m | 114 km | 537.4 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 270 | 1h 25m | 910 km | 4,236.9 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 260 | 28m | 304 km | 1,363.0 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 260 | 1h 10m | 770 km | 3,453.9 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 224 | 19m | 165 km | 637.2 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 218 | 26m | 275 km | 1,033.0 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 209 | 31m | - | - |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 163 | 20m | 99 km | 279.2 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 160 | 22m | 55 km | 152.1 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 159 | 27m | 215 km | 588.9 t |
| 16 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 17 | Bodø Airport (ENBO) | ENEN (ENEN) | 154 | 13m | - | - |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 151 | 27m | 152 km | 394.6 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 149 | 31m | 369 km | 948.4 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 147 | 44m | 452 km | 1,145.7 t |
| 21 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 144 | 18m | 144 km | 358.2 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 141 | 20m | 250 km | 609.0 t |
| 23 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 133 | 20m | 147 km | 336.6 t |
| 24 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 133 | 1h 1m | 695 km | 1,594.3 t |
| 25 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 133 | 44m | 241 km | 552.5 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 131 | 1h 43m | 1,423 km | 3,214.9 t |
| 27 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 131 | 1h 39m | 1,156 km | 2,613.4 t |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 124 | 1h 17m | 961 km | 2,055.4 t |
| 29 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 123 | 12m | - | - |
| 30 | Belgrade Nikola Tesla Airport (LYBE) | Berane Airport (LYBR) | 122 | 24m | 223 km | 469.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-06-14 09:43 UTC | 2026-06-14 09:54 UTC | 11m |
| CHX62 | CHX | Dresden Airport (EDDC) | Bautzen Airport (EDAB) | 2026-06-14 09:31 UTC | 2026-06-14 09:46 UTC | 14m |
| IGO1155 | IndiGo | Indira Gandhi International Airport (VIDP) | Tribhuvan International Airport (VNKT) | 2026-06-14 08:27 UTC | 2026-06-14 09:38 UTC | 1h 10m |
| AYT105 | AYT | Hatzor Air Base (LLHS) | Ein Yahav Airfield (LLEY) | 2026-06-14 09:16 UTC | 2026-06-14 09:35 UTC | 18m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-06-14 09:00 UTC | 2026-06-14 09:31 UTC | 30m |
| WIF454 | WIF | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 2026-06-14 09:02 UTC | 2026-06-14 09:28 UTC | 26m |
| HFA804 | HFA | Larnaca International Airport (LCLK) | LLBO (LLBO) | 2026-06-14 08:49 UTC | 2026-06-14 09:23 UTC | 33m |
| FHIBY | FHI | St Florentin Cheu Airport (LFGP) | St Florentin Cheu Airport (LFGP) | 2026-06-14 09:14 UTC | 2026-06-14 09:23 UTC | 8m |
| ICE16Y | ICE | Reykjavik Airport (BIRK) | Stykkishólmur Airport (BIST) | 2026-06-14 09:02 UTC | 2026-06-14 09:20 UTC | 17m |
| GCICK | GCI | Compton Abbas Aerodrome (EGHA) | Compton Abbas Aerodrome (EGHA) | 2026-06-14 09:14 UTC | 2026-06-14 09:18 UTC | 3m |
| HGO713 | HGO | East Midlands Airport (EGNX) | Zhuhai Airport (ZGSD) | 2026-06-13 21:46 UTC | 2026-06-14 09:17 UTC | 11h 31m |
| UAL2656 | United Airlines | Denver International Airport (KDEN) | General Edward Lawrence Logan International Airport (KBOS) | 2026-06-14 06:10 UTC | 2026-06-14 09:17 UTC | 3h 6m |
| WIF824 | WIF | Bodø Airport (ENBO) | ENEN (ENEN) | 2026-06-14 09:05 UTC | 2026-06-14 09:16 UTC | 10m |
| ZKIDU | ZKI | Invercargill Airport (NZNV) | Taieri Airport (NZTI) | 2026-06-14 08:20 UTC | 2026-06-14 09:16 UTC | 55m |
| GBILS | GBI | RAF Mona (EGOQ) | Caernarfon Airport (EGCK) | 2026-06-14 09:00 UTC | 2026-06-14 09:16 UTC | 15m |
| MAS8564 | Malaysia Airlines | Kuala Lumpur International Airport (WMKK) | Kroh Airport (WMBH) | 2026-06-14 08:35 UTC | 2026-06-14 09:12 UTC | 37m |
| VOE1ZP | VOE | Alicante International Airport (LEAL) | La Morgal Airport (LEMR) | 2026-06-14 08:06 UTC | 2026-06-14 09:12 UTC | 1h 5m |
| APG132 | APG | Ninoy Aquino International Airport (RPLL) | Kaohsiung International Airport (RCKH) | 2026-06-14 07:40 UTC | 2026-06-14 09:09 UTC | 1h 29m |
| GKEVX | GKE | Welshpool Airport (EGCW) | Shobdon Aerodrome (EGBS) | 2026-06-14 08:54 UTC | 2026-06-14 09:07 UTC | 13m |
| N428CF |  | Fort Worth Meacham International Airport (KFTW) | Mid-Way Regional Airport (KJWY) | 2026-06-14 08:52 UTC | 2026-06-14 09:07 UTC | 14m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
