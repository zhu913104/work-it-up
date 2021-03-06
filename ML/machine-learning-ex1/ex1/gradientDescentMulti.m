function [theta, J_history] = gradientDescentMulti(X, y, theta, alpha, num_iters)
%GRADIENTDESCENT Performs gradient descent to learn theta
%   theta = GRADIENTDESCENT(X, y, theta, alpha, num_iters) updates theta by 
%   taking num_iters gradient steps with learning rate alpha

% Initialize some useful values
m = length(y); % number of training examples
J_history = zeros(num_iters, 1);

n=size(X)(2);

s_gra=zeros(n,1);


for iter = 1:num_iters

    % ====================== YOUR CODE HERE ======================
    % Instructions: Perform a single gradient step on the parameter vector
    %               theta. 
    %
    % Hint: While debugging, it can be useful to print out the values
    %       of the cost function (computeCost) and gradient here.
    %
    %theta_grad=theta_grad+X'*(X*theta-y);
    %theta_alpha=theta_alpha+theta_grad.^2;
    %theta=theta-(alpha/m/theta_alpha.^0.5)*(X'*(X*theta-y));
    %theta=theta-(alpha/m)*(X'*(X*theta-y));

    gradJ = X'*(X*theta - y);
    s_gra=s_gra+gradJ.^2;
    ada = s_gra.^0.5;
    theta = theta - (alpha.*gradJ);
    

    %theta_alpha=theta_alpha+gradJ.^2;
    %theta = theta - alpha./(theta_alpha.^0.5) .* gradJ;
    % ============================================================

    % Save the cost J in every iteration    
    J_history(iter) = computeCost(X, y, theta);
    
end

end
