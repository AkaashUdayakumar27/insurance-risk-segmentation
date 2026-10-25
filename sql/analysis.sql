-- Overall claim frequency and loss cost
SELECT SUM(ClaimNb) * 1.0 / SUM(Exposure) AS frequency,
       SUM(ClaimAmount) / SUM(Exposure)   AS loss_cost
FROM policies;

