# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--20_18:01:59_UTC-green)

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

**Latest saved flight:** 2026-06-20 18:01:59 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-20 18:01:59 UTC

- **115,853** saved flights
- **40,134** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **115,853** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,408,941.0 tonnes** estimated CO2 emissions
- **81,677,741 km** total distance flown
- **861 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4777 |
| 2 | SkyWest Airlines | 4309 |
| 3 | EJA | 2245 |
| 4 | IndiGo | 2237 |
| 5 | American Airlines | 1811 |
| 6 | Southwest Airlines | 1725 |
| 7 | ENY | 1445 |
| 8 | Delta Air Lines | 1368 |
| 9 | Lufthansa | 1283 |
| 10 | Vueling | 1045 |
| 11 | WIF | 1024 |
| 12 | LATAM Airlines | 1019 |
| 13 | AZU | 965 |
| 14 | AXM | 953 |
| 15 | LXJ | 882 |
| 16 | Swiss International | 817 |
| 17 | All Nippon Airways | 792 |
| 18 | Alaska Airlines | 777 |
| 19 | QLK | 750 |
| 20 | easyJet | 742 |
| 21 | EJU | 728 |
| 22 | Cathay Pacific | 672 |
| 23 | AEE | 650 |
| 24 | VIV | 643 |
| 25 | United Airlines | 642 |
| 26 | Air France | 635 |
| 27 | CXK | 619 |
| 28 | MXY | 613 |
| 29 | AXB | 569 |
| 30 | GLO | 565 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 97903 |
| 2 | 🇪🇸 ES | 7895 |
| 3 | 🇮🇳 IN | 7048 |
| 4 | 🇦🇺 AU | 6860 |
| 5 | 🇧🇷 BR | 6381 |
| 6 | 🇮🇹 IT | 6197 |
| 7 | 🇩🇪 DE | 6174 |
| 8 | 🇨🇦 CA | 6089 |
| 9 | 🇯🇵 JP | 5185 |
| 10 | 🇬🇧 GB | 5039 |
| 11 | 🇫🇷 FR | 4599 |
| 12 | 🇨🇴 CO | 3985 |
| 13 | 🇲🇽 MX | 3418 |
| 14 | 🇬🇷 GR | 3306 |
| 15 | 🇳🇴 NO | 3186 |
| 16 | 🇨🇭 CH | 2956 |
| 17 | 🇲🇾 MY | 2470 |
| 18 | 🇹🇷 TR | 2346 |
| 19 | 🇿🇦 ZA | 1948 |
| 20 | 🇵🇱 PL | 1901 |
| 21 | 🇳🇿 NZ | 1899 |
| 22 | 🇰🇷 KR | 1882 |
| 23 | 🇹🇭 TH | 1881 |
| 24 | 🇵🇭 PH | 1682 |
| 25 | 🇬🇹 GT | 1637 |
| 26 | 🇲🇦 MA | 1259 |
| 27 | 🇲🇴 MO | 1169 |
| 28 | 🇲🇪 ME | 1141 |
| 29 | 🇳🇱 NL | 1118 |
| 30 | 🇭🇷 HR | 1005 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2448 |
| 2 | Denver International Airport |  | US | 1954 |
| 3 | Tokyo International Airport |  | JP | 1719 |
| 4 | Indira Gandhi International Airport |  | IN | 1545 |
| 5 | Guaymaral Airport |  | CO | 1475 |
| 6 | Harry Reid International Airport |  | US | 1451 |
| 7 | Eleftherios Venizelos International Airport |  | GR | 1419 |
| 8 | Zurich Airport |  | CH | 1289 |
| 9 | La Aurora Airport |  | GT | 1264 |
| 10 | Frankfurt am Main International Airport |  | DE | 1254 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1239 |
| 12 | El Dorado International Airport |  | CO | 1171 |
| 13 | Macau International Airport |  | MO | 1169 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1154 |
| 15 | Chicago O'Hare International Airport |  | US | 1140 |
| 16 | Capua Airport |  | IT | 1009 |
| 17 | Salt Lake City International Airport |  | US | 995 |
| 18 | Madrid Barajas International Airport |  | ES | 985 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 968 |
| 20 | Kuala Lumpur International Airport |  | MY | 954 |
| 21 | Congonhas Airport |  | BR | 887 |
| 22 | Charlotte/Douglas International Airport |  | US | 887 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 862 |
| 24 | Bengaluru International Airport |  | IN | 853 |
| 25 | General Edward Lawrence Logan International Airport |  | US | 852 |
| 26 | Charles de Gaulle International Airport |  | FR | 848 |
| 27 | Malpensa International Airport |  | IT | 825 |
| 28 | Ninoy Aquino International Airport |  | PH | 776 |
| 29 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 758 |
| 30 | Daniel K Inouye International Airport |  | US | 755 |
| 31 | Tenerife Norte Airport |  | ES | 752 |
| 32 | Barcelona International Airport |  | ES | 739 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 731 |
| 34 | Vitoria/Foronda Airport |  | ES | 684 |
| 35 | Don Mueang International Airport |  | TH | 682 |
| 36 | Calgary International Airport |  | CA | 680 |
| 37 | Amsterdam Airport Schiphol |  | NL | 679 |
| 38 | Seattle-Tacoma International Airport |  | US | 667 |
| 39 | Norman Y Mineta San Jose International Airport |  | US | 660 |
| 40 | Scottsdale Airport |  | US | 659 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 612 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 420 | 21m | 244 km | 1,768.5 t |
| 3 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 309 | 24m | 225 km | 1,198.8 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 299 | 9m | - | - |
| 5 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 286 | 1h 7m | 706 km | 3,482.1 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 283 | 1h 25m | 910 km | 4,440.9 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 281 | 14m | 114 km | 551.1 t |
| 8 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 275 | 1h 10m | 770 km | 3,653.2 t |
| 9 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 260 | 28m | 304 km | 1,363.0 t |
| 10 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 231 | 26m | 275 km | 1,094.6 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 227 | 19m | 165 km | 645.7 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 216 | 31m | - | - |
| 13 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 174 | 22m | 55 km | 165.4 t |
| 14 | Bodø Airport (ENBO) | ENEN (ENEN) | 169 | 13m | - | - |
| 15 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 168 | 20m | 99 km | 287.8 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 167 | 26m | 215 km | 618.5 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 157 | 27m | 152 km | 410.3 t |
| 18 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 154 | 31m | 369 km | 980.2 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 154 | 14m | 154 km | 408.0 t |
| 20 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 152 | 44m | 452 km | 1,184.6 t |
| 21 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 152 | 44m | 241 km | 631.4 t |
| 22 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 147 | 20m | 250 km | 635.0 t |
| 23 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 147 | 18m | 144 km | 365.7 t |
| 24 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 142 | 1h 44m | 1,423 km | 3,484.9 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 139 | 1h 1m | 695 km | 1,666.2 t |
| 26 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 135 | 1h 39m | 1,156 km | 2,693.2 t |
| 27 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 134 | 20m | 147 km | 339.1 t |
| 28 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 134 | 13m | - | - |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 132 | 1h 17m | 961 km | 2,188.0 t |
| 30 | Belgrade Nikola Tesla Airport (LYBE) | Berane Airport (LYBR) | 129 | 24m | 223 km | 496.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| GOLD4 | GOL | White Waltham Airfield (EGLM) | London City Airport (EGLC) | 2026-06-20 17:48 UTC | 2026-06-20 18:01 UTC | 13m |
| N15MJ |  | Palo Alto Airport (KPAO) | Tracy Municipal Airport (KTCY) | 2026-06-20 17:23 UTC | 2026-06-20 17:59 UTC | 35m |
| N201AD |  | Airlake Airport (KLVN) | Ankeny Regional Airport (KIKV) | 2026-06-20 16:45 UTC | 2026-06-20 17:57 UTC | 1h 11m |
| DHX729 | DHX | Bahrain International Airport (OBBI) | Zhuhai Airport (ZGSD) | 2026-06-20 10:12 UTC | 2026-06-20 17:54 UTC | 7h 42m |
| N88765 |  | Helio Airport (2AK7) | Talkeetna Airport (PATK) | 2026-06-20 17:25 UTC | 2026-06-20 17:47 UTC | 22m |
| SRG853A | SRG | Oban Airport (EGEO) | Glasgow International Airport (EGPF) | 2026-06-20 17:31 UTC | 2026-06-20 17:44 UTC | 13m |
| N480K |  | Juniper Airport (NV14) | Shepard Strip (07ID) | 2026-06-20 15:46 UTC | 2026-06-20 17:43 UTC | 1h 57m |
| N930SR |  | Lake Tahoe Airport (KTVL) | Rogers Field (KO05) | 2026-06-20 17:22 UTC | 2026-06-20 17:41 UTC | 19m |
| N530JL |  | North Las Vegas Airport (KVGT) | North Las Vegas Airport (KVGT) | 2026-06-20 16:08 UTC | 2026-06-20 17:38 UTC | 1h 30m |
| N100BW |  | Helio Airport (2AK7) | Talkeetna Airport (PATK) | 2026-06-20 17:18 UTC | 2026-06-20 17:38 UTC | 19m |
| N29230 |  | City Of Colorado Springs Municipal Airport (KCOS) | Tinnes Airport (CD03) | 2026-06-20 16:42 UTC | 2026-06-20 17:35 UTC | 53m |
| BLAST63 | BLA | Francisco de Sá Carneiro Airport (LPPR) | Francisco de Sá Carneiro Airport (LPPR) | 2026-06-20 16:58 UTC | 2026-06-20 17:35 UTC | 37m |
| N834KC |  | Knoxville Downtown Island Airport (KDKX) | Melton Field (4TN0) | 2026-06-20 17:30 UTC | 2026-06-20 17:34 UTC | 4m |
| N9506J |  | Solberg/Hunterdon Airport (KN51) | Linden Airport (KLDJ) | 2026-06-20 17:18 UTC | 2026-06-20 17:34 UTC | 16m |
| N5106D |  | Limon Municipal Airport (KLIC) | Limon Municipal Airport (KLIC) | 2026-06-20 17:17 UTC | 2026-06-20 17:34 UTC | 16m |
| N801JA |  | Pru Field (K33S) | Pru Field (K33S) | 2026-06-20 17:22 UTC | 2026-06-20 17:33 UTC | 10m |
| NDU659 | NDU | Mesa Gateway Airport (KIWA) | Eloy Municipal Airport (KE60) | 2026-06-20 16:44 UTC | 2026-06-20 17:31 UTC | 47m |
| AXEL21 | AXE | Robert Gray Army Air Field (KGRK) | Pueblo Memorial Airport (KPUB) | 2026-06-20 15:59 UTC | 2026-06-20 17:29 UTC | 1h 30m |
| N63FS |  | Clark Regional Airport (KJVY) | Morgantown Municipal/Walter L Bill Hart Field (KMGW) | 2026-06-20 16:43 UTC | 2026-06-20 17:29 UTC | 46m |
| TKR140 | TKR | AZ86 (AZ86) | Cottonwood Airport (KP52) | 2026-06-20 17:28 UTC | 2026-06-20 17:28 UTC | 0m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
